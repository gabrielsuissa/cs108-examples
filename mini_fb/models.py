from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Encapsulate the idea of a facebook profile (i.e., text).'''

    # data attributes of a quote:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this object.'''

        return "%s %s" % (self.first_name, self.last_name)

    
