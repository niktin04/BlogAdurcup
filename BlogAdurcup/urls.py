"""BlogAdurcup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import home.views as home_views
import blog.views as blog_views
import delight.views as delights_views
import newsmail.views as newsmail_views
import video.views as video_views
from django.http import HttpResponse

app_name = 'BlogAdurcup'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home_views.home, name='home'),
    url(r'^subscribe/$', home_views.subscribe, name='subscribe'),

    url(r'^home/', include('home.urls')),
    url(r'^blogs/', include('blog.urls')),
    url(r'^delights/', include('delight.urls')),
    url(r'^newsmails/', include('newsmail.urls')),
    url(r'^videos/', include('video.urls')),

    # AMP URLS
    url(r'^amp/$', home_views.home_amp, name='home_amp'),
    url(r'^amp/blogs$', blog_views.blogs_amp, name='blogs_amp'),
    url(r'^amp/blogs/(?P<blog_id>[0-9]+)/$', blog_views.blog_detail_amp, name='blog_detail_amp'),
    url(r'^amp/delights$', delights_views.delights_amp, name='delights_amp'),
    url(r'^amp/newsmails$', newsmail_views.newsmails_amp, name='newsmails_amp'),
    url(r'^amp/newsmails/(?P<newsmail_id>[0-9]+)/$', newsmail_views.newsmail_detail_amp, name='newsmail_detail_amp'),
    url(r'^amp/videos$', video_views.videos_amp, name='videos_amp'),

    # ROBOTS.TXT FILE CONFIG TO ALLOW ALL CRAWLERS AND ALL PAGES
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"),
        name="robots_file")
]
