# path: django/mini_amazon/admin.py
# author: gsuissa@bu.edu
# The admin page is used to update the Django admin interface for the models from models.py 
# to function. With that we can start creating the first Profiles, CartItems, Products and Shopping Carts

from django.contrib import admin

# Register your models here.

from .models import Profile, Product, CartItem, ShoppingCart 

# Adding each model one by one to the Django admin website
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(ShoppingCart)