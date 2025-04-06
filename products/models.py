from django.db import models
from cloudinary.models import CloudinaryField
from account.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('draft', 'Draft'),
            ('cancelled', 'Cancelled'),
        ]
    )
    shipping_address = models.TextField(blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()  # Consider validating this to match product price

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    methods = models.CharField(
        max_length=100,
        choices=[
            ('CBE', 'CBE'),
            ('telebirr', 'Telebirr'),
            ('awash bank', 'Awash Bank')
        ]
    )
    status = models.CharField(
        max_length=50,
        choices=[
            ('completed', 'Completed'),
            ('failed', 'Failed'),
            ('pending', 'Pending')
        ]
    )

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)