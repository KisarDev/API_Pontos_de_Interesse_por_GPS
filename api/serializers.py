from rest_framework import serializers
from rest_framework.schemas import AutoSchema

from api.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AddressSchema(AutoSchema):
    request_body = AddressSerializer