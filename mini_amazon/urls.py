# file: mini_amazon/urls.py
# description: direct URL requests to view functions 

from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # map the URL (empty string) to the view
    
    # Paths necessary for user login/logout system and authentification
    path("", auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),

    # Website principal pages  
    path('home', HomePageView.as_view(), name='home_page'), # home page that shows product selection 
    path('user/<int:pk>/shopping_cart', CartPageView.as_view(), name='cart_page'), # Shopping cart page
    path('product/<int:pk>', ShowProductPageView.as_view(), name='product_page'), # Product page
    path('all_products', ShowAllProductsPageView.as_view(), name='all_products_page'), # Show all products page
    path('user/<int:pk>', ShowProfilePageView.as_view(), name='user_page'), # User profile page
    
    # Paths necessary for ShoppingCart forms
    path('user/<int:pk>/shopping_cart/add_item', AddItemCartView.as_view(), name='add_item'), # URL for the  view
    # Path necessary to implement search bar 
    
]