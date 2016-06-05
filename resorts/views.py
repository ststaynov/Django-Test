from django.shortcuts import render

from blog.models import Blog, Category


def index(request):
    return render(request, 'resorts/index.html', {'categories': Category.objects.all(), 'posts': Blog.objects.all()[:5]})