from django.urls import path
from django.views.generic import TemplateView
from .views import ContactUsView, HomeView


app_name='home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', TemplateView.as_view(template_name='about-us.html'), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
]
