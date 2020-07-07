from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="博客标签")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = "博客标签"


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="博客分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = "博客分类"


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name="文章标题")
    author = models.ForeignKey(User, verbose_name="博客作者", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name="博客图片")
    body = models.TextField(verbose_name="博客正文")
    abstract = models.TextField(max_length=256, blank=True, null=True, verbose_name="博客摘要")
    visiting = models.PositiveIntegerField(default=9, verbose_name="访问量")
    category = models.ManyToManyField('Category', verbose_name="博客分类")
    tags = models.ManyToManyField('Tag', verbose_name="博客标签")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = "博客"
        verbose_name_plural = "博客"
