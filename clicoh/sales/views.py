"""Sales views."""

# Django
from django.shortcuts import render

# Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from .models import Order

# Serializers
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Order Model View Set."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #permission_classes = (IsAuthenticated,)
