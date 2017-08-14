from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=500, default='#')
    video_watch_url = models.CharField(max_length=1000, default='#')
    video_embed_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class VideoTag(models.Model):
    blog = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
