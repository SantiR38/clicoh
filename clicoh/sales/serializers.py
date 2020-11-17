"""Sales serializers."""

# Rest framework
from rest_framework import serializers

# Models
from .models import OrderDetail, Order

class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer."""

    class Meta:
        model = Order
        fields = ['id', 'date_time']


class OrderDetailSerializer(serializers.ModelSerializer):
    """Order Detail model serializer."""

    class Meta:
        model = OrderDetail
        fields = ['order', 'cuantity', 'price', 'product']