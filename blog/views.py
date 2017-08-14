from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Blog
from delight.models import Delight
from newsmail.models import NewsMail


# Create your views here.
def blogs(request):
    all_blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(all_blogs, 10)  # Shows number of records per page

    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delights_exceed = len(Delight.objects.all()) > 6
    last_6_newsmails = NewsMail.objects.all().order_by('-id')[:6]
    newsmails_exceed = len(NewsMail.objects.all()) > 6

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 7777), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'delights': last_6_delights,
        'delight_exceed': delights_exceed,
        'newsmails': last_6_newsmails,
        'newsmail_exceed': newsmails_exceed,
    }
    return render(request, 'blog/blogs.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)
