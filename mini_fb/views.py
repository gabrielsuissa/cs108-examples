from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.urls import reverse

# Create your views here.
class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all quotes.'''

    model = Profile # retrieve objects of type Quote from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles' # how to find the data in the template file

class ShowProfilePageView(DetailView): 
    """Create a subclass Profile view to display a profile."""

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile' # how to find the data in the template file

    def get_context_data(self, **kwargs):
        """Return the context data (a dictionary) to be used in the template."""

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context


class CreateProfileView(CreateView):
    """Create a subvlass of CreateView to display the form to create a new profile"""

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(UpdateView):
    """Create a subclass of UpdateView to display a form to update a profile."""

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()


def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''

    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']
        image = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        # save the new status message object to the database
        if image.is_valid() and message:

            image = image.save(commit=False) # create the object but not save it
            image.profile = profile
            image.save() # store to the database
            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            sm.save()

    else:
        print("Error: the form was not valid.")    
       
    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'profile_pk': pk}))


class DeleteStatusMessageView(DeleteView):
    """Creates a subclass of DeleteView"""

    template_name = 'mini_fb/delete_status_form.html'
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs): 
        """Return a dictionary with context data for this template to use."""

        # obtain default context data dictionary using super class version of get_class_context
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        status_message = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        profile = status_message.profile

        context['status_message'] = status_message
        context['profile'] = profile

        # return the context dictionary
        return context
    
    def get_success_url(self):
        """Returns the URL to which to redirect the user"""
        
        profile_pk = self.kwargs['pk']
        status_pk = self.kwargs['status_pk']
        return reverse('show_profile_page', kwargs={"pk":profile_pk})