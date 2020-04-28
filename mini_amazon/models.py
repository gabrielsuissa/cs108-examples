from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # will be used in login before entering the website
from datetime import datetime

# Create your models here.

# This model will represent a user's profile including necessary information to submit payments 
class Profile(models.Model):
    '''Encapsulate the idea of an amazon profile (i.e., text) except that we are adding the User model defined by Django'''

    # data attributes of a profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) # found online need to figure how it works
    city = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    credit_card = models.SmallIntegerField(blank=True) # optional will depend on time 

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.user.username, self.user.email)

    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("user_page", kwargs={"pk":self.pk})

    def get_shopping_cart(self):

        cart_user = ShoppingCart.objects.get(user=self)
        return cart_user
    
class Product(models.Model):
    """Encapsulates the idea of a product for sales"""

    #data attributes of a product
    product_name = models.TextField(blank=True)
    price = models.FloatField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.product_name, self.price)

    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("product_page", kwargs={"pk":self.pk})

class ShoppingCart(models.Model):
    """Encapsulate the idea of a Shopping Cart"""
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def get_items(self): 
        """Method to get all items"""

        query_set = CartItem.objects.filter(cart=self)

        return query_set

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s's cart" % (self.user)
   
class CartItem(models.Model):
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = Product.price
    cart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)

    def price_ttc(self):

        Tax_rate = 19.25
        return self.price_ht * (1 + Tax_rate /100.0)

    def __str__(self):
        return  str(self.product.product_name) + " - " + str(self.cart)

    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("product_page", kwargs={"pk":self.pk})

