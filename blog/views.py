from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from blog.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", context={"posts": posts})
