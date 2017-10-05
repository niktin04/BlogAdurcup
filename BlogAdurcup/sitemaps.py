from django.contrib.sitemaps import Sitemap
from blog.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return '/blogs/' + str(obj.id) + '/'

    def lastmod(self, obj):
        return obj.created_at
