# path: django/mini_amazon/models.py
# author: gsuissa@bu.edu
# This file is the foundation of the whole mini_amazon app. Models are made 
# to describe the essential features that will interact in the website

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # will be used in login before entering the website
from datetime import datetime

# Create your models here.


# This model will represent a user's profile including essential attributes to characterize a profile
class Profile(models.Model):
    '''Encapsulate the idea of an amazon profile (i.e., text) except that we are adding the User model defined by Django'''

    # data attributes of a profile

    # This links the Profile model to the built-in User model from Django. The User model will set the 
    # username and password system as well as the pk to describe each profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
    # The last two attributes are less important but add to the richness of mini_amazon's content
    city = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    credit_card = models.SmallIntegerField(blank=True)

    # __str__ functions are used to give the string representation in the Django Admin interface
    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.user.username, self.user.email)

    # This function is used to get a valuable url to display for each profile
    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''

        return reverse("user_page", kwargs={"pk":self.pk})

    # This method gives a way to simplify later queries 
    def get_shopping_cart(self):
        '''A function to select the cart that correspond to a user'''

        cart_user = ShoppingCart.objects.get(user=self) # get function returns only one object
        return cart_user


class Product(models.Model):
    """Encapsulates the idea of a product for sale, (name, price and image)"""

    #data attributes of a product
    product_name = models.TextField(blank=True)
    price = models.FloatField(blank=True)
    image_url = models.URLField(blank=True)

    # __str__ functions are used to give the string representation in the Django Admin interface
    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.product_name, self.price)

    # This function is used to get a valuable url to display for each profile
    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("product_page", kwargs={"pk":self.pk})


class ShoppingCart(models.Model):
    """Encapsulate the idea of what a Shopping Cart is (ie container of CartItems specific to a user)"""
    
    # data attributes of a ShoppingCart
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    # This method gives a way to simplify later queries 
    def get_items(self): 
        """Method to get all items that correspind to a ShoppingCart"""

        query_set = CartItem.objects.filter(cart=self) # filter is used to get CartItems (class bellow) that are part of a specific ShoppingCart

        return query_set

    # __str__ functions are used to give the string representation in the Django Admin interface
    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s's cart" % (self.user)


class CartItem(models.Model):
    
    #data attributes of a CartItem
    product = models.OneToOneField(Product, on_delete=models.CASCADE) # CartItem correspond to one product
    quantity = models.IntegerField(default=1) # CartItem must specify a quantity
    cart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE) # a Cartitem belongs to one ShoppingCart
    user = ShoppingCart.user

    # __str__ functions are used to give the string representation in the Django Admin interface
    def __str__(self):
        return  str(self.product.product_name) + " - " + str(self.cart)

    # This function is used to get a valuable url to display for each profile
    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("cart_page", kwargs={"pk":self.pk})
