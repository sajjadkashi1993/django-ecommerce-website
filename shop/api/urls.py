from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('product/', include("product.api.urls")),
    path('cart/', include("cart.api.urls")),
    path('order/', include("order.api.urls")),
    path('accounts/', include("accounts.api.urls")),
    path('api-token-auth/', views.obtain_auth_token)

]
