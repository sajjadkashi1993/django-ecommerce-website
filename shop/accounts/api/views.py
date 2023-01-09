from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from ..models import Address
from .serializers import AddressSerilizers


class AddressCustomerListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AddressSerilizers

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressCustomerAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AddressSerilizers

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
