from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path("notification/", consumers.NotificationConsumer.as_asgi()),
]


