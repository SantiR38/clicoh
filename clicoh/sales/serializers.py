"""Sales serializers."""

# Rest framework
from rest_framework import serializers

# Models
from .models import OrderDetail, Order
from clicoh.products.models import Product

# Serializers
from clicoh.products.serializers import ProductSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    """Order Detail model serializer."""
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Product.objects.all(),
        source='product'
        )
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderDetail
        fields = ['cuantity', 'price', 'product', 'product_id']
        read_only = ['price']
    
    def validate_cuantity(self, value):
        """
        Check that the cuantity is > 0.
        """
        if value <= 0:
            raise serializers.ValidationError("The cuantity should be greater than zero")
        return value
    
    def get_price(self, obj):
        return OrderDetail.get_product_price(obj.product)


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer."""
    price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'date_time', 'price']

    def get_price(self, obj):
        return Order.get_total(obj)


class OrderDetailedSerializer(OrderSerializer):
    """Order model serializer."""
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'date_time', 'details', 'price']

    def create(self, validated_data):
        """Allows to create details in the same order view."""

        details_data = validated_data.pop('details')
        order = Order.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetail.objects.create(order=order, **detail_data)
        return order