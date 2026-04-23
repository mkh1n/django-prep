from django.contrib import admin
from .models import Product, Supplier, Category, Manufacturer
# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Manufacturer)