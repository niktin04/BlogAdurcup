from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=100, default='Adurcup')
    title = models.CharField(max_length=500)
    summary = models.TextField(default='#')
    content = RichTextField()
    img_url = models.CharField(max_length=1000, default='#')
    img_alt_tag = models.CharField(max_length=500, default="Plastic Packaging")
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + ': ' + self.comment
