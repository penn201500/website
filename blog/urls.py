"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:blog_id>/', views.detail, name='blog_detail'),
    path('category/<int:category_id>/', views.category, name='blog_category'),
    path('tag/<int:tag_id>/', views.tag, name='blog_tag'),
    path('search/', views.search, name='blog_search'),
    path('archive/<int:year>/<int:month>/', views.archive, name='blog_archive'),
]
