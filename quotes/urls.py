# file: quotes/urls.py
# description: direct URL requests to view functions 

from django.urls import path
from .views import HomePageView

urlpatterns = [
    # map the URL (empty string) to the view
    path('', HomePageView.as_view(), name='home'), # generic class based view
]