from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = '../templates/pages/home.html'

class AboutPageView(TemplateView):
    template_name = '../templates/pages/about.html'

