from django.views.generic import TemplateView


class HomePageTemplateView(TemplateView):
    template_name = "pages/home.html"
