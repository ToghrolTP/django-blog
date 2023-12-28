from django.shortcuts import render
from .models import Post


def post_list(request):
    available_posts = Post.published.all()
    context = {
        "posts": available_posts,
    }
    return render(request, "blog/post/list.html", context)
