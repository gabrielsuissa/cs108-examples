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
    model = Profile
    template_name = 'mini_amazon/user_page.html'
    context_object_name = 'profile' # how to find the data in the template file


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

class HomePageView(TemplateView):
    """create a subclass of ListView to display our home page"""
    template_name = 'mini_amazon/home_page.html'


# All the Views related to the Shopping Cart

class CartPageView(DetailView):
    """Create a subclass of ListView to display Shopping cart"""
    model = Profile
    template_name = 'mini_amazon/cart_page.html'
    context_object_name = 'profile'

class DeleteItemCartView(DeleteView):
    model = ShoppingCart
    template_name = 'cart/delete_cart.html'

class AddItemCartView(UpdateView):
    
    form_class = BuyItemForm
    template_name = 'mini_amazon/add_item_form.html'
    queryset = CartItem.objects.all()

    # def get_context_data(self, **kwargs): 
    #     """Return a dictionary with context data for this template to use."""

    #     # obtain default context data dictionary using super class version of get_class_context
    #     context = super(AddItemCartView, self).get_context_data(**kwargs)

    #     product = Product.objects.get(pk=self.kwargs['cart_pk'])
    #     cart = ShoppingCart.user

    #     context['product'] = product
    #     context['cart'] = cart

    #     # return the context dictionary
    #     return context

# View to make the search bar using the Q (query function built in Django)
