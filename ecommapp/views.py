# from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
