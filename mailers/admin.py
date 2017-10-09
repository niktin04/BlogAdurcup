from django.contrib import admin
from .models import Mailers, SendMails

# Register your models here.
# admin.site.register(Mailers)
admin.site.register(Mailers)
admin.site.register(SendMails)
