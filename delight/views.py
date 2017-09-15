from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Delight
from newsmail.models import NewsMail

# Create your views here.
def delights(request):
    all_delights = Delight.objects.all().order_by('-id')
    paginator = Paginator(all_delights, 10)  # Shows number of records per page

    last_6_newsmail = NewsMail.objects.all().order_by('-id')[:6]
    newsmail_exceed = len(NewsMail.objects.all()) > 6
    amp_url = 'http://blog.adurcup.com/amp/delights/'

    page = request.GET.get('page')
    try:
        delights = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        delights = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 7777), deliver last page of results.
        delights = paginator.page(paginator.num_pages)

    context = {
        'delights': delights,
        'newsmails': last_6_newsmail,
        'newsmail_exceed': newsmail_exceed,
        'amp_url': amp_url,
    }

    return render(request, 'delight/delights.html', context)


def delights_amp(request):
    all_delights = Delight.objects.all().order_by('-id')
    amp_url = 'http://blog.adurcup.com/delights/'

    context = {
        'delights': all_delights,
        'amp_url': amp_url,
    }

    return render(request, 'delight/delights_amp.html', context)
