# file: mini_fb/urls.py
# description: direct URL requests to view functions 

from django.urls import path
from .views import * #ShowAllProfilesView, ShowProfilePageView, CreateProfileView, CreateProfileForm, UpdateProfileForm, UpdateProfileView, create_status_message

urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'), # generic class based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # URL for one profile
    path('profile/<int:pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_status'), # URL for one profile
    path('create_profile', CreateProfileView.as_view(), name='create_profile'), # URL for the create profile view
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), # URL for the update profile view
    path('profile/<int:pk>/post_status', create_status_message, name='post_status'), # URL for the update profile view
]

