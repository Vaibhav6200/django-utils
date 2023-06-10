from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    song_duration = models.IntegerField(    )
    user = models.ManyToManyField(User)

    def writtenBy(self):
        return ",".join([str(p) for p in self.user.all()])



class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
