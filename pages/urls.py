# coding=utf-8
from django.urls import path

import pages.views

urlpatterns = [
    path('', pages.views.HomePageView.as_view(), name='homepage'),
]
