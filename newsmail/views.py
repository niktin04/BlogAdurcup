from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from delight.models import Delight
from .models import NewsMail


# Create your views here.
def newsmails(request):
    all_newsmails = NewsMail.objects.all().order_by('-id')
    paginator = Paginator(all_newsmails, 10)  # Shows number of records per page

    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delight_exceed = len(Delight.objects.all()) > 6
    amp_url = 'http://blog.adurcup.com/amp/newsmails/'

    page = request.GET.get('page')
    try:
        newsmails = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        newsmails = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 7777), deliver last page of results.
        newsmails = paginator.page(paginator.num_pages)

    context = {
        'newsmails': newsmails,
        'delights': last_6_delights,
        'delight_exceed': delight_exceed,
        'amp_url': amp_url,
    }
    return render(request, 'newsmail/newsmails.html', context)


def newsmails_amp(request):
    all_newsmails = NewsMail.objects.all().order_by('-id')
    amp_url = 'http://blog.adurcup.com/newsmails/'

    context = {
        'newsmails': all_newsmails,
        'amp_url': amp_url,
    }
    return render(request, 'newsmail/newsmails_amp.html', context)


def newsmail_detail(request, newsmail_id):
    newsmail = get_object_or_404(NewsMail, id=newsmail_id)
    amp_url = 'http://blog.adurcup.com/amp/newsmails/' + newsmail_id + '/'

    context = {
        'newsmail': newsmail,
        'amp_url': amp_url,
    }
    return render(request, 'newsmail/newsmail_detail.html', context)

def newsmail_detail_amp(request, newsmail_id):
    newsmail = get_object_or_404(NewsMail, id=newsmail_id)
    amp_url = 'http://blog.adurcup.com/newsmails/' + newsmail_id + '/'
    context = {
        'newsmail': newsmail,
        'amp_url': amp_url,
    }
    return render(request, 'newsmail/newsmail_detail_amp.html', context)
