from django.contrib import admin

# Register your models here.

from .models import Profile, Product, CartItem, ShoppingCart
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(ShoppingCart)
