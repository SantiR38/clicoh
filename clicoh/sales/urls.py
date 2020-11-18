"""Sales urls."""

# Django
from django.urls import path, include

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views

router = DefaultRouter()
router.register(r'', views.OrderViewSet, basename='sale')
router.register(r'order_detail', views.OrderDetailedViewSet, basename='sale_detail')

urlpatterns = [

    path('', include(router.urls))

]