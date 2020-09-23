from django.contrib.syndication.views import Feed
from .models import Post


class LatestEntriesFeed(Feed):
    title = "My Blogs"
    link = "/site_blogs/"
    description = "latest test feed"

    @staticmethod
    def items():
        return Post.objects.order_by('-created_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract
