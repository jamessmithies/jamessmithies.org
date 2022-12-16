from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Entry

class LatestEntriesFeed(Feed):
    title = "jamessmithies.org/blog RSS"
    link = "/blog/rss/"
    description = "Updates on blog posts on jamessmithies.org."

    def items(self):
        return Entry.objects.order_by('-pub_date')[:100]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

 