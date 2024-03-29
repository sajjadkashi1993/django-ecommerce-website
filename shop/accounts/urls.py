from django.urls import include, path
from .views import LoginRegisteruser, VerifyCodeview, LogoutView, Accontview, ProfileFormView

app_name='accounts'
urlpatterns = [
    path('login/', LoginRegisteruser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/', VerifyCodeview.as_view(), name='verify'),
    path('account/', Accontview.as_view(), name='account'),
    path('account/update/', ProfileFormView.as_view(), name='account_update'),

]