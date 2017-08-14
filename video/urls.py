from django.conf.urls import url
from . import views

app_name = 'video'

urlpatterns = [
    # /videos/
    url(r'^$', views.videos, name="videos"),
]