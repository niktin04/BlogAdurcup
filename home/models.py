from django.db import models


# Create your models here.
class Welcome(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=1000, default='#')
    img_alt_tag = models.CharField(max_length=500, default="Plastic Packaging")

    def __str__(self):
        return self.title


class Quote(models.Model):
    quote = models.CharField(max_length=1000)
    author = models.CharField(max_length=100, default='#')

    def __str__(self):
        return self.author


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email