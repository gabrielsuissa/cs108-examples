# file: quotes/urls.py
# description: direct URL requests to view functions 

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageview

urlpatterns = [
    # map the URL (empty string) to the view
    path('', RandomQuotePageview.as_view(), name="random"), # pick one quote at random
    path('all', HomePageView.as_view(), name='home'), # generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # Show one quote
] 