# file: quotes/urls.py
# description: direct URL requests to view functions 

from django.urls import path
from .views import * # HomePageView, QuotePageView, RandomQuotePageview, PersonPageView

urlpatterns = [
    # map the URL (empty string) to the view
    path('', RandomQuotePageview.as_view(), name="random"), # pick one quote at random
    path('all', HomePageView.as_view(), name='all'), # generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # Show one quote
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), # Show one person
    path('create', CreateQuoteView.as_view(), name='create'), # create a new quote with a form

] 