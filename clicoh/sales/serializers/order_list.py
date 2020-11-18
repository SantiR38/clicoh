"""Sales list serializers."""

# Rest framework
from rest_framework import serializers

# Models
from clicoh.sales.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer."""
    price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'date_time', 'price']

    def get_price(self, obj):
        """Get the total price of the entire order."""

        return Order.get_total(obj)