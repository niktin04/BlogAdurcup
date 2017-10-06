from django.db import models
from datetime import datetime
from django.contrib.sitemaps import ping_google


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

    def save(self, *args, **kwargs):
        if not self.id:
            self.published_at = datetime.now()
        self.updated_at = datetime.now()

        super(Video, self).save(*args, **kwargs)

        try:
            ping_google('http://blog.adurcup.com/sitemap.xml')
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

        return super(Video, self).save(*args, **kwargs)


class VideoTag(models.Model):
    blog = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
