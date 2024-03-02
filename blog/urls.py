"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# blog\urls.py

from django.contrib import admin
from django.urls import path

# <адрес_сайта>/blog/*
from blog import views

app_name = "blog"

urlpatterns = [
    # <адрес_сайта>/blog/
    path('', views.index, name="index"),
    # <адрес_сайта>/blog/auth/
    path('auth_page/', views.auth_page, name="auth"),
    path('auth/', views.auth, name="authorize"),
    path('deauth/', views.deauth, name="logout"),

    path('register_page/', views.register_page, name="register_page"),
    path('register/', views.register, name="register"),

    path('post/<int:post_id>', views.view_post, name="view_post")
]
