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


@register.simple_tag()
def get_most_visited_entries(num=5):
    """
    获取访问最多的博客，默认5个
    :param num:
    :return:
    """
    blogs = Post.objects.all().order_by('-visiting')
    if len(blogs) >= num:
        return Post.objects.all().order_by('-visiting')[:num]
    else:
        return Post.objects.all()


@register.simple_tag()
def get_categories_entries():
    """
    获取所有分类
    :param num:
    :return:
    """
    return Category.objects.all()


@register.simple_tag()
def get_count_of_category(category_id):
    return Post.objects.filter(category=category_id).count()


@register.simple_tag()
def get_categories_entries():
    """
    获取所有分类
    :param num:
    :return:
    """
    return Category.objects.all()


@register.simple_tag()
def get_archive_entries():
    """
    归档
    :return:
    """
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag()
def get_count_of_archive(year, month):
    return Post.objects.filter(created_time__year=year, created_time__month=month).count()


@register.simple_tag()
def get_tags_entries():
    return Tag.objects.all()


@register.simple_tag()
def get_count_of_tag(tag_id):
    return Post.objects.filter(tags=tag_id).count()
