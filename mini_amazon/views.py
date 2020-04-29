# path: django/mini_amazon/views.py
# author: gsuissa@bu.edu
# This page is necessary to display each page on the website and link each element of the webpages to a form and/or model 

from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import *

# Create your views here.


class ShowProfilePageView(DetailView): 
    """Create a subclass DetailView view to display a profile."""

    model = Profile # The model that corresponds
    template_name = 'mini_amazon/user_page.html' # The template file
    context_object_name = 'profile' # how to find the data in the template file


class ShowProductPageView(DetailView): 
    """Create a subclass Detail view to display a product."""

    model = Product # The model that corresponds
    template_name = 'mini_amazon/product_page.html' # The template file
    context_object_name = 'product' # how to find the data in the template file


    # This function is necessary to link the buy button to the BuyItem Form
    def get_context_data(self, **kwargs): 
        """Return a dictionary with context data for this template to use."""

        # obtain default context data dictionary using super class version of get_class_context
        context = super(ShowProductPageView, self).get_context_data(**kwargs)

        Item = BuyItemForm() # This is creating a new BuyItemForm Object
        context['item_form'] = Item # This adds it to a new dictionary

        # return the context dictionary
        return context


class ShowAllProductsPageView(ListView): 
    """Create a subclass List view to display a all products."""

    model = Product # The model that corresponds
    template_name = 'mini_amazon/all_products_page.html' # The template file
    context_object_name = 'all_products' # how to find the data in the template file


class HomePageView(TemplateView):
    """create a subclass of ListView to display our home page"""
    
    # A very simple page that requires no model linkage

    template_name = 'mini_amazon/home_page.html' # The template file


class CartPageView(DetailView):
    """Create a subclass of ListView to display Shopping cart"""

    model = Profile # The model that corresponds
    template_name = 'mini_amazon/cart_page.html' # The template file
    context_object_name = 'profile' # how to find the data in the template file


# View classes or functions that are related to forms 



class UpdateProfileView(UpdateView):
    """Create a subclass of UpdateView to display a form to update a profile."""

    form_class = UpdateProfileForm
    template_name = 'mini_amazon/update_profile_form.html'
    queryset = Profile.objects.all()


def add_item(request, pk):
    '''Process a form submission to add an item to the user's cart.'''

    # find the profile that matches the `pk` in the URL
    user = User.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        quantity = request.POST['quantity']
        product = request.POST['product']
        cart = request.POST['cart']
        form = BuyItemForm(request.POST)

        # save the proper data in the database
        # Not completed just a list of failed ideas
        # form = CartItem()
        # cart = CartItem.cart
        # form.save()
            
        # quantity = CartItem()
        # product = CartItem()
        # cart = CartItem()


            # quantity.product = None
            # quantity.quantity = 1
            # quantity.cart = None

            # product.product = Product()
            # product.quantity = None
            # product.cart = None

            # cart.product = None
            # cart.quantity = None
            # cart.cart = ShoppingCart()

            # quantity.save()
            # cart.save()
            # product.save()

    else:
        print("Error: the form was not valid.")    
        
    # redirect the user to the cart_page view
    return redirect(reverse('cart_page', kwargs={'pk': user.pk})) 


# class DeleteItemCartView(DeleteView):
#     """A view that links to the DeleteItem Form using the default DeleteView"""

#     model = ShoppingCart # The model that corresponds
#     template_name = 'cart/delete_cart.html' # The template file
