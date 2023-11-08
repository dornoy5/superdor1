from django.db import models
from django.conf import settings

class Customer(models.Model):
    customer_id = models.BigIntegerField(unique=True)  # changed from DecimalField to BigIntegerField
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return self.name 

class Category(models.Model):
    description = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to='categories/', blank=True, null=True, default='אין.jpg')

    def __str__(self):
        return self.description if self.description else "Category"

class Product(models.Model):
    description = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    img = models.ImageField(upload_to='products/', blank=True, null=True, default='אין.jpg')

    def __str__(self):
        return self.description if self.description else "Product"

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')