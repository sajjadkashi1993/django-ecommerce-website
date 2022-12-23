from django.urls import include, path

urlpatterns = [
    path('product/', include("product.api.urls")),
]
