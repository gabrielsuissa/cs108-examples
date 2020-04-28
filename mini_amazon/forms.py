from django import forms
from .models import Profile, Product, ShoppingCart, CartItem
from django.contrib.auth.models import User

class BuyItemForm(forms.ModelForm):
    """A form to add an item in the cart"""

    quantity = forms.IntegerField(label="Quantity", required=True)

    class Meta:
        '''associate this form with the CartItem model'''
        model = CartItem
        fields = ['product', 'quantity', 'cart', ]

