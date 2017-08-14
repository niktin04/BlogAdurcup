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

app_name = 'BlogAdurcup'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home_views.home, name='home'),
    url(r'^subscribe/', home_views.subscribe, name='subscribe'),

    url(r'^home/', include('home.urls')),
    url(r'^blogs/', include('blog.urls')),
    url(r'^delights/', include('delight.urls')),
    url(r'^newsmails/', include('newsmail.urls')),
    url(r'^videos/', include('video.urls')),
]
