from django.contrib import admin
from .models import Product, Category, Customer

admin.site.register([Product,Category,Customer])