from django import template
from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag()
def get_latest_entries(num=5):
    """
    获取最近博客，默认5个
    :param num:
    :return:
    """
    blogs = Post.objects.all().order_by('-created_time')
    if len(blogs) >= num:
        return Post.objects.all().order_by('-created_time')[:num]
    else:
        return Post.objects.all()
