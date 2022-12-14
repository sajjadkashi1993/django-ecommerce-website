from django.urls import include, path
from .views import LoginRegisteruser, VerifyCodeview


app_name='accounts'
urlpatterns = [
    path('login/', LoginRegisteruser.as_view(), name='login'),
    path('verify/', VerifyCodeview.as_view(), name='verify'),

]