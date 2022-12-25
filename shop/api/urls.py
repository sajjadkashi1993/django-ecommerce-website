from django.urls import include, path

urlpatterns = [
    path('product/', include("product.api.urls")),
    path('cart/', include("cart.api.urls")),
]
