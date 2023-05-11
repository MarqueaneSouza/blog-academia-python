from django.http import HttpResponse
from django.shortcuts import render
from . models import Post


# Create your views here.
def home(request):
    #return HttpResponse('<h1> Hello, World!! </h1>') #antes do template ser criado
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

def blog(request):
    return render(request, 'blog/blog.html')