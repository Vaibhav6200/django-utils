from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer
from .models import *
import json
from django.contrib.auth.models import User

# Step1: create a function that will be used to create a notification object on every event


# group_add: creates a room group by the name of "test_consumer_group" where all notifications will be sent
# group_send: will be used to broadcast these events inside of the "test_consumer_group"
# get_user: takes id as input and returns if theres a user against it from database
# create_notification: will create a notification object for that user
# send_notification: Now the way notifications are sent to the front end is where the "send_notification" method comes into play

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except:
        pass
        # return AnonymousUser()


@database_sync_to_async
def create_notification(receiver, typeof="task_created", status="unread"):
    notification_to_create = Notifications(user_revoker=receiver, type_of_notification=typeof)
    notification_to_create.save()
    print("I am here to help")
    return (notification_to_create.user_revoker, notification_to_create.type_of_notification)


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, event):
        print(event)
        data_to_get = json.loads(event['text'])
        user_to_get = await get_user(int(data_to_get))
        print(user_to_get)
        get_of = await create_notification(user_to_get)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_notification",
                "value": json.dumps(get_of)
            }
        )

        print("receive", event)

    async def disconnect(self, event):
        print("disconnect", event)

    async def send_notification(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))

        print("I am here")
        print(event)