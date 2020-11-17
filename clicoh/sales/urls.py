"""Sales urls."""

# Django
from django.urls import path, include

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views

router = DefaultRouter()
router.register(r'', views.OrderViewSet, basename='sale')

urlpatterns = [

    path('', include(router.urls))

]