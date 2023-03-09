
from django.contrib import admin
from .models import  Product, Size, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Size)