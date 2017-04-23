from django.shortcuts import render
from plainbox.impl.unit import category

from blog.models import Blog, Category
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.filter(type='post').order_by('-id')[:5],
        'pages': Blog.objects.filter(type='page'),
    })


def view_post(request, slug):
    return render_to_response('blog/view_post.html', {
        'pages': Blog.objects.filter(type='page'),
        'categories': Category.objects.all(),
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    # print("dd")
    # exit()
    category = Category.objects.filter(slug=slug)
    return render_to_response('blog/view_category.html' )
