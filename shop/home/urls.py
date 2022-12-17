from django.urls import path
from django.views.generic import TemplateView
from .views import ContactUsView


app_name='home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about-us/', TemplateView.as_view(template_name='about-us.html'), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
]
