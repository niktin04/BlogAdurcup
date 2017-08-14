from django.conf.urls import url
from . import views

app_name = 'newsmail'

urlpatterns = [
    # /newsmails/
    url(r'^$', views.newsmails, name="newsmails"),

    # /newsmails/1234/
    url(r'^(?P<newsmail_id>[0-9]+)/$', views.newsmail_detail, name="newsmail_detail"),
]