from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", context={"posts": posts})


# <адрес_сайта>/blog/post/<int:post_id>
def view_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound(f"Post with id: {post_id} does not exist.")

    return render(request, "post.html", context={"post": post})
