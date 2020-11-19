"""Sales models."""

# Django
from django.db import models


class Order(models.Model):
    """Order model."""
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()

    @classmethod
    def get_total(self, obj):
        """Get total method.

        Calculate the total price of the order.
        """
        details = OrderDetail.objects.filter(order=obj)
        return sum([i.price * i.cuantity for i in details])


class OrderDetail(models.Model):
    """Order Detail model.

    Primary key will be created automatically and inevitably.
    """

    order = models.ForeignKey('sales.Order', related_name='details', on_delete=models.CASCADE)
    cuantity = models.PositiveIntegerField()
    price = models.FloatField(null=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    
    @classmethod
    def get_product_price(cls, obj, product):
        """Get product price,

        and put it on the order detail price.
        """
        obj.price = product.price
        obj.save()
        return obj.price