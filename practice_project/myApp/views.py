import datetime
from django.shortcuts import render
from django.core.cache import caches
from django.contrib.auth.models import User
from .models import *



cache = caches['chat_cache']


def cache_chat_messages(messages, room_id):
    mess = []
    for message in messages:
        cache_key = f"{room_id}-{message.id}"
        cache.get_or_set(cache_key, message, 10)
        x = cache.get_or_set(cache_key, None)
        mess.append(x)
    return mess


def index(request):
    chatroom = ChatRoom.objects.get(room_id=12345)
    messages = ChatMessage.objects.filter(room=chatroom).order_by('created_at')
    mess = cache_chat_messages(messages, chatroom.room_id)
    return render(request, 'home.html', {"messages": mess})



def get_cached_chat_messages(room_id):
    chat_messages = cache.get(room_id)
    if chat_messages is None:
        chat_messages = ChatMessage.objects.filter(room_id=room_id).order_by('created_at')

        # Remove chat messages that are older than 24 hours
        chat_messages = [message for message in chat_messages if message.created_at > datetime.now() - datetime.timedelta(hours=24)]

        cache.set(room_id, chat_messages, timeout=60*60*24) # 24 hours
    return chat_messages


# def cache_chat_messages(chat_messages):
#     for chat_message in chat_messages:
#         key = f'chat_message_{chat_message.id}'
#         cache.set(key, chat_message, timeout=60*60*24) # 24 hours

