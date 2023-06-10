from django.contrib import admin
from .models import *


@admin.register(Song)
class CustomSong(admin.ModelAdmin):
    list_display = ['id', 'song_name', 'song_duration', 'writtenBy']

@admin.register(Publication)
class CustomSong(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Article)
class CustomSong(admin.ModelAdmin):
    list_display = ['id', 'headline']