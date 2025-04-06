from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    ProductViewSet,
    CartViewSet,
    CartItemViewSet,
    OrderViewSet,
    OrderItemViewSet,
    WishlistViewSet,
    PaymentViewSet
)

app_name = 'products'

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('cart', CartViewSet, basename='cart')
router.register('cart-item', CartItemViewSet)
router.register('order', OrderViewSet)
router.register('order-item', OrderItemViewSet)
router.register('wishlist', WishlistViewSet)
router.register('payment', PaymentViewSet)

urlpatterns = [
     path('', include(router.urls)),  # Ensure the trailing slash is correct
]