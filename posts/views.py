from django.views.generic import ListView
from posts.models import Post


class HomePageView(ListView):
    model = Post
    template_name = '../templates/posts/home.html'
