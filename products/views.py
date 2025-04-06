from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    Product,
    CartItem,
    Cart,
    Order,
    OrderItem,
    Wishlist,
    WishlistItem,
    Payment
)
from .serializers import *


class ProductViewSet(ModelViewSet):
    # permission_classes =[IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(ModelViewSet):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get_object(self):
        cart, created = Cart.objects.get_or_create(user = self.request.user)
        
        return cart


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)
    
    def perform_create(self, serializer):
        user = self.request.user
        
        cart , created = Cart.objects.get_or_create(user=user)
        serializer.save(cart=cart)
        


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(order__user=self.request.user)
    
class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    
# def get_cart(request):
#     user = request.user
    
#     item, created = Cart.objects.get_or_create(user)
#     cart_item = CartItem.objects.create(item)