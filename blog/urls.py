from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    # /blogs/
    url(r'^$', views.blogs, name="blogs"),

    # /blogs/1234/
    url(r'^(?P<blog_id>[0-9]+)/$', views.blog_detail, name="blog_detail"),

    # /blogs/12345/comment
    url(r'^(?P<blog_id>[0-9]+)/comment$', views.comment, name="blog_comment"),
]
