from django.shortcuts import reverse
from django.contrib.sitemaps import Sitemap
from main_app.models import Feed, SiteData


class SiteDataSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weelky'

    def items(self):
        datalist = SiteData.objects.filter().order_by("-updated")[:1]
        return datalist

    def location(self, item):
        return reverse("landing")


class FeedSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Feed.objects.filter(display=True).order_by("-updated")

    @staticmethod
    def lastmod(obj):
        return obj.updated

    def location(self, item):
        return reverse("feed")
