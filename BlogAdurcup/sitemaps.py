from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Blog
from delight.models import Delight
from newsmail.models import NewsMail
from video.models import Video


class BlogsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return '/blogs/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class BlogsAmpSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return '/amp/blogs/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class DelightsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Delight.objects.all()

    def location(self, obj):
        return '/delights/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class DelightsAmpSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Delight.objects.all()

    def location(self, obj):
        return '/amp/delights/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class NewsmailsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return NewsMail.objects.all()

    def location(self, obj):
        return '/newsmails/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class NewsmailsAmpSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return NewsMail.objects.all()

    def location(self, obj):
        return '/amp/newsmails/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class VideosSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Video.objects.all()

    def location(self, obj):
        return '/videos/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class VideosAmpSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Video.objects.all()

    def location(self, obj):
        return '/amp/videos/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['index', 'home:home', 'blog:blogs', 'delight:delights', 'newsmail:newsmails', 'video:videos',
                'subscribe', 'unsubscribe', 'unsubscribe_email', 'index_amp', 'home_amp', 'blogs_amp', 'delights_amp',
                'newsmails_amp', 'videos_amp']

    def location(self, item):
        return reverse(item)
