from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from .models import Mailers


# Create your views here.
def mailers_form(request):
    all_blogs = Blog.objects.all().order_by('-id')

    context = {
        'blogs': all_blogs,
    }
    return render(request, 'mailers/update_mailer_form.html', context)


def update_mailer(request):
    all_blogs = Blog.objects.all().order_by('-id')

    context = {
        'blogPrimary': all_blogs,
        'blogSecondary': all_blogs,
        'blogTertiary': all_blogs,
    }
    return render(request, 'mailers/update_mailer.html', context)


def mailer_check(request, mailer_id):
    mailer = get_object_or_404(Mailers, id=mailer_id)
    context = {
        'blog_data': mailer,
    }
    return render(request, 'mailers/mailer_mail_update_template.html', context)
