# coding=utf-8
from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.BlogListView.as_view(), name='blogpage'),
    path('<int:pk>/', blog.views.BlogDetailView.as_view(), name='blogdetail'),  # new
]
