from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    '''Encapsulate the idea of a facebook profile (i.e., text).'''

    # data attributes of a profile
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        '''Return  a URL to display this profile object.'''
        return reverse("show_profile_page", kwargs={"pk":self.pk})
    
    def get_status_messages(self): 
        '''Return  a URL to display  this quote object.'''
        status = StatusMessage.objects.filter(profile=self.pk)
        return status



class StatusMessage(models.Model):
    """Models the data attributes of Facebook status messages."""

    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        """return a string representation of this object """
        return '%s %s %s' % (self.profile, self.message, self.timestamp)
    