from django.contrib import admin
from .models import Welcome, Quote, Subscribe, Unsubscribe

# Register your models here.
admin.site.register(Welcome)
admin.site.register(Quote)
admin.site.register(Subscribe)
admin.site.register(Unsubscribe)
