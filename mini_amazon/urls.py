# file: mini_amazon/urls.py
# author: gsuissa@bu.edu
# description: direct URL requests to view functions. This page is necessary to organize the website's arboresence 
# and is needed to apply a view function to each page

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

    # Website's main pages  
    path('home', HomePageView.as_view(), name='home_page'), # home page  
    path('user/<int:pk>/shopping_cart', CartPageView.as_view(), name='cart_page'), # Shopping cart page
    path('product/<int:pk>', ShowProductPageView.as_view(), name='product_page'), # Product page
    path('all_products', ShowAllProductsPageView.as_view(), name='all_products_page'), # Shows all products page
    path('user/<int:pk>', ShowProfilePageView.as_view(), name='user_page'), # User's profile page
    
    # Paths necessary for ShoppingCart forms
    path('user/<int:pk>/shopping_cart/add_item', add_item, name='add_item'), # URL used to add_item function

    # Paths necessary to Profile forms
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), # URL for the update profile view
    
]