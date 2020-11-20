"""Sales views."""

# Django
#from django.shortcuts import render

# Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
#from rest_framework.permissions import IsAuthenticated

# Models
from .models import Order

# Serializers
from .serializers.order_list import OrderSerializer
from .serializers.order_detail import OrderDetailedSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Order Model View Set."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #permission_classes = (IsAuthenticated,)


class OrderDetailedViewSet(viewsets.ModelViewSet):
    """Order Model View Set."""

    queryset = Order.objects.all()
    serializer_class = OrderDetailedSerializer
    #permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=["POST"])
    def post(self, request):
        """Post actions."""
        
        serializer = OrderDetailedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
