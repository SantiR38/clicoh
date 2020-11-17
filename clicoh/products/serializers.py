"""Products serializers."""

# Rest framework
from rest_framework import serializers

# Models
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product model serializer."""

    class Meta:
        model = Product
        fields = ['id', 'name', 'price']