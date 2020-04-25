from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Profile, Product, ShoppingCart
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

class ShowProfilePageView(DetailView): 
    """Create a subclass DetailView view to display a profile."""

    model = Profile
    template_name = 'mini_amazon/user_page.html'
    context_object_name = 'profile' # how to find the data in the template file

class LoginPageView(DeleteView):

    model = User
    template_name = 'mini_amazon/login_page.html'
    context_object_name = ''

    # def get_context_data(self, **kwargs):
    #     """Return the context data (a dictionary) to be used in the template."""

    #     # obtain the default context data (a dictionary) from the superclass; 
    #     # this will include the Profile record for this page view
    #     context = super(ShowProfilePageView, self).get_context_data(**kwargs)
    #     # create a new CreateStatusMessageForm, and add it into the context dictionary
    #     form = CreateStatusMessageForm()
    #     context['create_status_form'] = form
    #     # return this context dictionary
    #     return context

class ShowProductPageView(DetailView): 
    """Create a subclass Detail view to display a product."""

    model = Product
    template_name = 'mini_amazon/product_page.html'
    context_object_name = 'product' # how to find the data in the template file

class ShowAllProductsPageView(ListView): 
    """Create a subclass List view to display a all products."""

    model = Product
    template_name = 'mini_amazon/all_products_page.html'
    context_object_name = 'all_products' # how to find the data in the template file

class HomePageView(ListView):
    """create a subclass of ListView to display our home page"""

    template_name = 'mini_amazon/home_page.html'

