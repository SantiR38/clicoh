"""Sales models."""

# Django
from django.db import models


class Order(models.Model):
    """Order model.

    Primary key will be created automatically and inevitably.
    """
    date_time = models.DateTimeField()

    @classmethod
    def get_total(self, obj):
        """Get total method.

        Calculate the total price of the order.
        """
        details = OrderDetail.objects.filter(order=obj)
        return sum([i.product.price * i.cuantity for i in details])


class OrderDetail(models.Model):
    """Order Detail model.

    Primary key will be created automatically and inevitably.
    """

    order = models.ForeignKey('sales.Order', related_name='details', on_delete=models.CASCADE)
    cuantity = models.IntegerField()
    price = models.FloatField()
    product = models.OneToOneField('products.Product', on_delete=models.CASCADE)

    def __str__(self):
        """Order Detail string representation."""

        return '%d, %s, %f' % (self.cuantity, self.product, self.price)
    
    @classmethod
    def get_product_price(cls, product):
        """Get product price,

        and put it on the order detail price.
        """

        return product.price