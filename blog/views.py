from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    entries = models.Post.objects.all()
    return render(request, 'blog/index.html', locals())


def detail(request, blog_id):
    return render(request, 'blog/detail.html', locals())
