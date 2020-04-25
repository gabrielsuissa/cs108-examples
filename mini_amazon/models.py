from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # will be used in login before entering the website

# Create your models here.

# This model will represent a user's profile including necessary information to submit payments 
class Profile(User):
    '''Encapsulate the idea of a facebook profile (i.e., text).'''

    # data attributes of a profile
    #user = models.OneToOneField(User, on_delete=models.CASCADE) # found online need to figure how it works
    # first_name = models.TextField(blank=True)
    # last_name = models.TextField(blank=True)
    # email_address = models.EmailField(blank=True)
    new_field = models.CharField(max_length=140, null=True)
    city = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    credit_card = models.SmallIntegerField(blank=True) # optional will depend on time 

    def _get_pk_val(self):
        '''Defines pk value'''

        self.user_ptr_id = self.pk

        return self.pk

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


