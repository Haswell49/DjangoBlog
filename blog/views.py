from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect

from blog.forms import LoginForm, RegisterForm
from blog.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", context={"posts": posts})


def register_page(request):
    if request.method != "GET":
        return HttpResponse(status=405)

    return render(request, "register.html")


def register(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    register_form = RegisterForm(request.POST)

    if not register_form.is_valid():
        return HttpResponse(status=500, content=b"Register form is not valid.",
                            charset="utf-8")

    if register_form.cleaned_data["password"] != register_form.cleaned_data["password_confirm"]:
        return HttpResponse(status=500,
                            content=b"password and password_confirm do not match.",
                            charset="utf-8")

    # from django.contrib.auth.models import User
    user = User(username=register_form.cleaned_data["username"],
                email=register_form.cleaned_data["email"],
                first_name=register_form.cleaned_data["first_name"],
                last_name=register_form.cleaned_data["last_name"])

    user.set_password(register_form.cleaned_data["password"])

    user.save()

    login(request, user)

    return redirect("blog:index")


def auth_page(request):
    if request.method != "GET":
        return HttpResponse(status=405)

    return render(request, "auth.html")


def auth(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    login_form = LoginForm(request.POST)

    if not login_form.is_valid():
        return HttpResponse(status=500,
                            content=b"Invalid user form data.",
                            charset="utf-8")

    user = authenticate(username=login_form.cleaned_data["username"],
                        email=login_form.cleaned_data["email"],
                        password=login_form.cleaned_data["password"])

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
