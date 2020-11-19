"""Sales serializers."""

# Rest framework
from rest_framework import serializers

# Serializers
from clicoh.products.serializers import ProductSerializer

# Models
from clicoh.products.models import Product
from clicoh.sales.models import OrderDetail, Order


class DetailSerializer(serializers.ModelSerializer):
    """Order Detail model serializer."""
    product_id = serializers.CharField()
    product = ProductSerializer(read_only=True)
    #price = serializers.SerializerMethodField()

    class Meta:
        model = OrderDetail
        fields = ['cuantity', 'price', 'product_id', 'product']
        read_only_fields = ['price']

    def validate_cuantity(self, value):
        """
        Check that the cuantity is > 0.
        """
        if value <= 0:
            raise serializers.ValidationError("The cuantity should be greater than zero")
        return value
    
    def get_product(self):
        """Get the product from his id."""
        
        return Product.objects.get(id=self.product_id)
'''
    def get_price(self, obj):
        """Get the price for every detail."""
        product = Product.objects.get(id=obj.id)

        return OrderDetail.get_product_price(obj, product)
'''

class OrderDetailedSerializer(serializers.ModelSerializer):
    """Order model serializer."""
    id = serializers.IntegerField(read_only=True)
    details = DetailSerializer(many=True)
    price = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        """Allows to create details in the same order view."""

        details_data = validated_data.pop('details') # Extrae la parte del detail del json
        order = Order.objects.create(**validated_data) # Crea un objeto order a partir de todo el json
        for detail_data in details_data: # Crea objetos de tipo order_detail a partir de details_data
            
            # Bring the product so we can put it as foreign key in order detail
            product_data = detail_data.pop('product_id')
            product = Product.objects.get(id=product_data)
            
            order_detail = OrderDetail.objects.create(order=order, product=product, **detail_data)
            order_detail.price = OrderDetail.get_product_price(order_detail, product)
            order_detail.save()

    class Meta:
        model = Order
        fields = ['id', 'date_time', 'details', 'price']


    def get_price(self, obj): # Obj is an order dict with the serializer data. It's not a db object.
        """Get the total price of the entire order."""
        order = Order.objects.get(id=self.id)

        return Order.get_total(order)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
