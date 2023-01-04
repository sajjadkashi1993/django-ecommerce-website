from rest_framework import serializers
from ..models import Address


class AddressSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

  