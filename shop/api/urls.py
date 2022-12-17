from django.urls import include, path

urlpatterns = [
    path('v1/product/', include("product.api.urls")),
]
