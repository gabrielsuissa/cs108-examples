from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # will be used in login before entering the website

# Create your models here.

# This model will represent a user's profile including necessary information to submit payments 
class Profile(models.Model):
    '''Encapsulate the idea of an amazon profile (i.e., text) except that we are adding the User model defined by Django'''

    # data attributes of a profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) # found online need to figure how it works
    #user_ptr_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, db_constraint=True, related_name="Ma", default="")
    username = User.username
    email = User.email
    city = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    credit_card = models.SmallIntegerField(blank=True) # optional will depend on time 

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.username, self.email)

    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("user_page", kwargs={"pk":self.pk})
    
class Product(models.Model):
    """Encapsulates the idea of a product for sales"""

    #data attributes of a product
    product_name = models.TextField(blank=True)
    price = models.SmallIntegerField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.product_name, self.price)

    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("product_page", kwargs={"pk":self.pk})

class ShoppingCart(models.Model):
    """Encapsulates the idea of a shopping cart"""

    # data attributes of a shopping cart
    Profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    Products = models.ManyToManyField(Product)

    # probably will add some form to process it and redirect toward a "confirmation page"


