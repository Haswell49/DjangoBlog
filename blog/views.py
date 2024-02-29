from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect

from blog.forms import UserForm
from blog.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", context={"posts": posts})


def auth_page(request):
    if request.method == "GET":
        return render(request, "auth.html")
    elif request.method == "POST":
        user_form = UserForm(request.POST)

        if not user_form.is_valid():
            return HttpResponse(status=500,
                                content=b"Invalid user form data.",
                                charset="utf-8")

        user = authenticate(username=user_form.cleaned_data["username"],
                            email=user_form.cleaned_data["email"],
                            password=user_form.cleaned_data["password"])

        if user:
            login(request, user)
            return redirect("blog:index")
        else:
            return redirect("blog:auth")


def deauth(request):
    if request.method != "GET":
        return HttpResponse(status=500, content=b"Invalid HTTP method.")

    user = request.user

    if user.is_anonymous:
        return redirect("blog:index")

    logout(request)

    return redirect("blog:index")


# <адрес_сайта>/blog/post/<int:post_id>
def view_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound(f"Post with id: {post_id} does not exist.")

    return render(request, "post.html", context={"post": post})
