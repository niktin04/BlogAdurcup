from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from delight.models import Delight
from newsmail.models import NewsMail
from django.contrib import messages


# Create your views here.
def blogs(request):
    all_blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(all_blogs, 10)  # Shows number of records per page

    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delights_exceed = len(Delight.objects.all()) > 6
    last_6_newsmails = NewsMail.objects.all().order_by('-id')[:6]
    newsmails_exceed = len(NewsMail.objects.all()) > 6
    amp_url = 'http://blog.adurcup.com/amp/blogs/'

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
        'amp_url': amp_url,
    }
    return render(request, 'blog/blogs.html', context)


def blogs_amp(request):
    all_blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(all_blogs, 10)  # Shows number of records per page

    last_6_delights = Delight.objects.all().order_by('-id')[:6]
    delights_exceed = len(Delight.objects.all()) > 6
    last_6_newsmails = NewsMail.objects.all().order_by('-id')[:6]
    newsmails_exceed = len(NewsMail.objects.all()) > 6
    amp_url = 'http://blog.adurcup.com/blogs/'

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
        'amp_url': amp_url,
    }
    return render(request, 'blog/blogs_amp.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    amp_url = 'http://blog.adurcup.com/amp/blogs/' + blog_id + '/'
    context = {
        'blog': blog,
        'amp_url': amp_url,
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_detail_amp(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    amp_url = 'http://blog.adurcup.com/blogs/' + blog_id + '/'
    context = {
        'blog': blog,
        'amp_url': amp_url,
    }
    return render(request, 'blog/blog_detail_amp.html', context)


def comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    message = request.POST['message']
    name = request.POST['name']
    email = request.POST['email']

    if len(email) and len(name) and len(message):
        comment_obj = Comment(blog=blog, comment=message, name=name, email=email)
        comment_obj.save()
        messages.success(request, 'Comment added successfully.')
    else:
        messages.info(request, 'Oops! Some error occurred while adding your comment.')

    return redirect(request.META.get('HTTP_REFERER') + '#comments-section')
