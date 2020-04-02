# quotes/forms.py

from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    '''A form to add new quotes to the database.'''

    class Meta:
        '''associate this form with the Quote model.'''
        model = Quote
        fields = ['person', 'text', ] # which fields from the model should we use
        