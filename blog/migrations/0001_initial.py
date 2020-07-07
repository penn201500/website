# Generated by Django 3.0.8 on 2020-07-07 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='博客分类')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='博客标签')),
            ],
            options={
                'verbose_name': '博客标签',
                'verbose_name_plural': '博客标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='文章标题')),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='博客图片')),
                ('body', models.TextField(verbose_name='博客正文')),
                ('abstract', models.TextField(blank=True, max_length=256, null=True, verbose_name='博客摘要')),
                ('visiting', models.PositiveIntegerField(default=9, verbose_name='访问量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='博客作者')),
                ('category', models.ManyToManyField(to='blog.Category', verbose_name='博客分类')),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='博客标签')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'ordering': ['-created_time'],
            },
        ),
    ]
