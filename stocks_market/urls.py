from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockDataViewSet

# Create a router instance
router = DefaultRouter()
router.register('stockdata', StockDataViewSet, basename='stockdata')

# Include the router-generated URLs
urlpatterns = [
    path('', include(router.urls)),
]
