from django.views.generic import ListView
from posts.models import PostsDB


class HomePageView(ListView):
    model = PostsDB
    template_name = '../templates/posts/home.html'
    context_object_name = 'post_list'

