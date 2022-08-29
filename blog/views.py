
from django.shortcuts import render
from .models import Post


# Create your views here.

def index(requset, request=None):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
