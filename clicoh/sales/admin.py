"""Sales admin."""

# Django
from django.contrib import admin

# Models
from .models import Order, OrderDetail

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order model admin."""

    list_display = ('id', 'date_time')


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    """OrderDetail model admin."""

    list_display = ('order', 'cuantity', 'price', 'product')