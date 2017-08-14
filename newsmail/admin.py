from django.contrib import admin
from .models import NewsMail, NewsMailTag

# Register your models here.
admin.site.register(NewsMail)
admin.site.register(NewsMailTag)
