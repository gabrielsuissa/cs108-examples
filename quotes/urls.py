# file: quotes/urls.py
# description: direct URL requests to view functions 

from django.urls import path
from .views import * # HomePageView, QuotePageView, RandomQuotePageview, PersonPageView

urlpatterns = [
    # map the URL (empty string) to the view
    path('', RandomQuotePageview.as_view(), name="random"), # pick one quote at random
    path('all', HomePageView.as_view(), name='all'), # generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # Show one quote
    path('quote/<int:pk>/update_quote', UpdateQuoteView.as_view(), name='update_quote'), # Update a quote
    path('quote/<int:pk>/delete_quote', DeleteQuoteView.as_view(), name='delete_quote'), # Delete a quote
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), # Show one person
    path('person/<int:pk/add_image>', add_image, name='add_image'), # Add an image to a person
    path('create_quote', CreateQuoteView.as_view(), name='create_quote'), # create a new quote with a form

] 