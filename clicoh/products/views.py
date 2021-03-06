"""Product views."""

# Django
from django.shortcuts import render

# Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from .models import Product

# Serializers
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Product Model View Set."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = (IsAuthenticated,)
