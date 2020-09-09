from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    entries = Post.objects.all()
    return render(request, 'blog/index.html', locals())


def detail(request, blog_id):
    entry = Post.objects.get(id=blog_id)
    entry.increase_visiting()
    return render(request, 'blog/detail.html', locals())
