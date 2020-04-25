from django import forms
from .models import Profile, Product, ShoppingCart
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    """A new form that will help users create a new profile """

    # first_name = forms.CharField(label="First Name", required=True)
    # birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1918,-1),),)
    
    class Meta:
        '''associate this form with the User model.'''
        model = User
        fields = ['username', 'password', ] # which fields from the model should we use