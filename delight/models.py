from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Delight(models.Model):
    number = models.CharField(max_length=10, default='#001')
    author = models.CharField(max_length=100, default='Adurcup')
    content = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=1000, default='#')
    img_alt_tag = models.CharField(max_length=500, default="Plastic Packaging")
    published_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.number + ' - ' + self.content[:70] + '...'

    def save(self, *args, **kwargs):
        if not self.id:
            self.published_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Delight, self).save(*args, **kwargs)
