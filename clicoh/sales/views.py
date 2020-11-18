"""Sales views."""

# Django
#from django.shortcuts import render

# Rest Framework
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated

# Models
from .models import Order

# Serializers
from .serializers.order_list import OrderSerializer
#from .serializers.order_detail import OrderDetailedSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Order Model View Set."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #permission_classes = (IsAuthenticated,)

'''
class OrderDetailedViewSet(viewsets.ModelViewSet):
    """Order Model View Set."""

    queryset = Order.objects.all()
    serializer_class = OrderDetailedSerializer
    #permission_classes = (IsAuthenticated,)
'''