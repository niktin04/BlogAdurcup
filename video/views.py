from django.shortcuts import render
from .models import Video
from delight.models import Delight
from newsmail.models import NewsMail

# Create your views here.
def videos(request):
    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delights_exceed = len(Delight.objects.all()) > 6
    last_6_newsmails = NewsMail.objects.all().order_by('-id')[:6]
    newsmails_exceed = len(NewsMail.objects.all()) > 6
    all_videos = Video.objects.all().order_by('-id')
    amp_url = 'http://blog.adurcup.com/amp/videos/'

    context = {
        'delights': last_6_delights,
        'delight_exceed': delights_exceed,
        'newsmails': last_6_newsmails,
        'newsmail_exceed': newsmails_exceed,
        'videos': all_videos,
        'amp_url': amp_url,
    }

    return render(request, 'video/videos.html', context)


def videos_amp(request):
    all_videos = Video.objects.all().order_by('-id')
    amp_url = 'http://blog.adurcup.com/videos/'

    context = {
        'videos': all_videos,
        'amp_url': amp_url,
    }

    return render(request, 'video/videos_amp.html', context)