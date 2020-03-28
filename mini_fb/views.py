from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all quotes.'''

    model = Profile # retrieve objects of type Quote from the database
    template_name = 'templates.html'
    context_object_name = 'all_profiles' # how to find the data in the template file

