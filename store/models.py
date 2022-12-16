from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Stationary', 'Stationary'),
        ('Electronics', 'Electronics'),
        ('Food', 'Food'),
        ('Health', 'Health')
    )
    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=350)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=70, choices=CATEGORY_CHOICES, default=1)
    
    def __str__(self):
        return self.name
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name="orderitem", on_delete=models.CASCADE, null=True, blank=True)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.seller_id} - {self.product}'
    
    
    