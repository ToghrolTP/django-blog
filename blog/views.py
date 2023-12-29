from django.shortcuts import render
from django.http import Http404
from .models import Post


def post_list(request):
    available_posts = Post.published.all()
    context = {
        "posts": available_posts,
    }
    return render(request, "blog/post/list.html", context)


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    context = {
        "post": post,
    }
    return render(request, "blog/post/detail.html", context)
