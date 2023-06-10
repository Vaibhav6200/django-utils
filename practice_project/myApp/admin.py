from django.contrib import admin
from .models import *


class CustomChatRoom(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'room_id']

class CustomChatMessage(admin.ModelAdmin):
    list_display = ['id', 'sender', 'room', 'message_content', 'created_at']


admin.site.register(ChatRoom, CustomChatRoom)
admin.site.register(ChatMessage, CustomChatMessage)