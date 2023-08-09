from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogDB


class BlogListView(ListView):
    model = BlogDB
    template_name = '../templates/blog/home.html'
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):  # new
    model = BlogDB
    template_name = '../templates/blog/detail.html'