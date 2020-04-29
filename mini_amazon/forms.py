# path: django/mini_amazon/forms.py
# author: gsuissa@bu.edu
# This page allows for mini_amazon to use custom versions of the forms.ModelForm 
# application in Django 

from django import forms
from .models import Profile, Product, ShoppingCart, CartItem
from django.contrib.auth.models import User


class BuyItemForm(forms.ModelForm):
    """A form to add an item in the cart"""

    # We can customize the way each field is being displayed
    # IntegerField for quantity makes obvious sense, it is also required
    quantity = forms.IntegerField(label="Quantity", required=True, show_hidden_initial=1) 
    product = Product.objects.filter() # Selecting the item to buy
    cart = forms.widgets.Select() # Selecting the cart to which the new Item must be added

    class Meta:
        '''associate this form with the CartItem model'''
        model = CartItem # The model with which we link the form
        fields = ['product', 'quantity', 'cart', ] # these are the fields that the form must contain


class UpdateProfileForm(forms.ModelForm):
    """A new form that allows updating an existing profile"""

    class Meta:
        '''associate this form with the Profile model.'''
        model = Profile
        fields = ['city', 'image_url', 'credit_card', ] # which fields from the model should we use
