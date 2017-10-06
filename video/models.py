from django.db import models
from datetime import datetime


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=500, default='#')
    video_watch_url = models.CharField(max_length=1000, default='#')
    video_embed_url = models.CharField(max_length=1000)
    published_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.published_at.strftime("%d-%m-%Y %H:%M") + ' --- ' + self.title + ' --- ' + self.updated_at.strftime(
            "%d-%m-%Y %H:%M")


class VideoTag(models.Model):
    blog = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
