from django.contrib.sitemaps import Sitemap, GenericSitemap
from blog.models import Post
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['/', 'about']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changfreq = "always"
    priority = 1.0

    def items(self):
        return ['christa', 'john']

    def location(self, item):
        return reverse("blog_author", args=[item])


sitemaps = {
    'blogPost': GenericSitemap({
        'queryset': Post.objects.all(),
        'date_field': 'last_modified',
    }, priority=0.9),
    'blog': BlogSitemap,
    'static': StaticViewSitemap,
}
