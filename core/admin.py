from django.contrib import admin
from core.models import Product, Seller, Seller_Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Seller)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Seller_Product)
class ProviderAdmin(admin.ModelAdmin):
    pass