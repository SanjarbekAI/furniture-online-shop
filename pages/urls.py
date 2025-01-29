from django.urls import path

from pages.views import HomePageTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home')
]
