from django.shortcuts import render, redirect
from .models import Welcome, Quote, Subscribe, Unsubscribe
from blog.models import Blog
from delight.models import Delight
from newsmail.models import NewsMail
from video.models import Video
from django.contrib import messages


# Create your views here.
def home(request):
    welcome = Welcome.objects.last()
    quote = Quote.objects.last()
    last_6_blogs = Blog.objects.all().order_by('-id')[:6]
    blogs_exceed = len(Blog.objects.all()) > 6
    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delights_exceed = len(Delight.objects.all()) > 6
    last_6_newsmails = NewsMail.objects.all().order_by('-id')[:6]
    newsmails_exceed = len(NewsMail.objects.all()) > 6
    last_2_videos = Video.objects.all().order_by('-id')[:2]
    video_exceed = len(Video.objects.all()) > 2
    amp_url = 'http://blog.adurcup.com/amp/home/'

    context = {
        'welcome': welcome,
        'quote': quote,
        'blogs': last_6_blogs,
        'blog_exceed': blogs_exceed,
        'delights': last_6_delights,
        'delight_exceed': delights_exceed,
        'newsmails': last_6_newsmails,
        'newsmail_exceed': newsmails_exceed,
        'videos': last_2_videos,
        'video_exceed': video_exceed,
        'amp_url': amp_url,
    }

    return render(request, 'home/home.html', context)


def home_amp(request):
    welcome = Welcome.objects.last()
    quote = Quote.objects.last()
    last_6_blogs = Blog.objects.all().order_by('-id')[:6]
    blogs_exceed = len(Blog.objects.all()) > 6
    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delights_exceed = len(Delight.objects.all()) > 6
    last_6_newsmails = NewsMail.objects.all().order_by('-id')[:6]
    newsmails_exceed = len(NewsMail.objects.all()) > 6
    last_2_videos = Video.objects.all().order_by('-id')[:2]
    video_exceed = len(Video.objects.all()) > 2
    amp_url = 'http://blog.adurcup.com/amp/home/'

    context = {
        'welcome': welcome,
        'quote': quote,
        'blogs': last_6_blogs,
        'blog_exceed': blogs_exceed,
        'delights': last_6_delights,
        'delight_exceed': delights_exceed,
        'newsmails': last_6_newsmails,
        'newsmail_exceed': newsmails_exceed,
        'videos': last_2_videos,
        'video_exceed': video_exceed,
        'amp_url': amp_url,
    }

    return render(request, 'home/home_amp.html', context)


def unsubscribe(request):
    return render(request, 'home/unsubscribe.html')


def subscribe(request):
    email = request.POST['email']

    if len(email):
        subs_obj = Subscribe(email=email)
        subs_obj.save()

        if Unsubscribe.objects.filter(email=email):
            Unsubscribe.objects.filter(email=email).delete()

        messages.success(request, 'Email successfully subscribed.')
    else:
        messages.info(request, 'Enter a valid email address.')

    return redirect(request.META.get('HTTP_REFERER') + '#subscribe')


def unsubscribe_email(request):
    email = request.POST['email']

    if len(email):
        if Subscribe.objects.filter(email=email):
            unsubs_obj = Unsubscribe(email=email)
            unsubs_obj.save()
            Subscribe.objects.filter(email=email).delete()
            messages.success(request, 'Email successfully unsubscribed.')
            return redirect('http://blog.adurcup.com/')
        else:
            messages.info(request, 'Enter a registered email address.')
    else:
        messages.info(request, 'Enter a valid email address.')

    return redirect(request.META.get('HTTP_REFERER'))
