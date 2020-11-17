"""Products urls."""

# Django
from django.urls import path, include

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')

urlpatterns = [

    path('', include(router.urls))

]