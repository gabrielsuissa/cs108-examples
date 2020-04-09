from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):
    """A new form that will help users create a new profile """

    first_name = forms.CharField(label="First Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1918,-1),),)
    
    class Meta:
        '''associate this form with the Profile model.'''
        model = Profile
        fields = ['first_name', 'last_name', 'email_address', 'city', 'image_url', ] # which fields from the model should we use

class UpdateProfileForm(forms.ModelForm):
    """A new form that allows updating an existing profile"""

    class Meta:
        '''associate this form with the Profile model.'''
        model = Profile
        fields = ['first_name', 'last_name', 'email_address', 'city', 'image_url', ] # which fields from the model should we use

class CreateStatusMessageForm(forms.ModelForm):
    """A new form that will enable profiles to publish new status."""

    message = forms.CharField(label="Message", required=True)
    image = forms.ImageField(label="Image", required=False)
    class Meta:
        '''associate this form with the StatusMessage model.'''
        model = StatusMessage
        fields = ['message', 'image', ] # which fields from the model should we use
