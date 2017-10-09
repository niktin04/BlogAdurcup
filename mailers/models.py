from django.db import models
from django.shortcuts import redirect

from blog.models import Blog


# Create your models here.
class Mailers(models.Model):
    primaryBlog = Blog.objects.all().order_by('-id')[0]
    secondaryBlog = Blog.objects.all().order_by('-id')[1]
    tertiaryBlog = Blog.objects.all().order_by('-id')[2]

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        super(Mailers, self).save(*args, **kwargs)
        redirect("http://blog.adurcup.com/mailers/" + str(self.id))
