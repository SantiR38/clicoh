"""Sales models."""

# Django
from django.db import models


class Order(models.Model):
    """Order model.

    Primary key will be created automatically and inevitably.
    """

    date_time = models.DateTimeField()

    @classmethod
    def get_total(cls, order_id):
        """Get total method.

        Calculate the total price of the order.
        """
        order = cls.objects.get(id=order_id)
        details = OrderDetail.objects.filter(order=order)

        return sum([i.price * i.cuantity for i in details])


class OrderDetail(models.Model):
    """Order Detail model.

    Primary key will be created automatically and inevitably.
    """

    order = models.ForeignKey('sales.Order', on_delete=models.CASCADE)
    cuantity = models.IntegerField()
    price = models.FloatField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)