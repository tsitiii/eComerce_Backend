from rest_framework.serializers import ModelSerializer
from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Wishlist,
    WishlistItem,
    Payment
)

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistItemSerializer(ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'