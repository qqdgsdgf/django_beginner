# coding=utf-8
from django.urls import path
import posts.views

urlpatterns = [
    path('', posts.views.HomePageView.as_view(), name='postspage'),
]
