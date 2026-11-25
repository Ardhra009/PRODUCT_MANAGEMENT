from rest_framework import serializers
from productapp.models import ProductDB

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDB
        fields = "__all__"