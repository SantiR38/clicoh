"""Sales serializers."""

# Rest framework
from rest_framework import serializers

# Models
from .models import OrderDetail, Order


class OrderDetailSerializer(serializers.ModelSerializer):
    """Order Detail model serializer."""
    #product = 
    #price = 

    class Meta:
        model = OrderDetail
        fields = ['cuantity', 'price', 'product']
        read_only = ['price']


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer."""
    details = OrderDetailSerializer(many=True)
    price = Order.get_total(cls.id)

    class Meta:
        model = Order
        fields = ['id', 'date_time', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        order = Order.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetail.objects.create(order=order, **detail_data)
        return order