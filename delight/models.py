from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Delight(models.Model):
    number = models.CharField(max_length=10, default='#001')
    content = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=1000, default='#')
    img_alt_tag = models.CharField(max_length=500, default="Plastic Packaging")

    def __str__(self):
        return self.number + ' - ' + self.content[:70] + '...'
