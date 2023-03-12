"""
user.py file
User model class
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    
    # Отчество
    second_name = models.CharField(max_length=150, blank=True, verbose_name=_('second name')) 
    
    def get_full_name(self):
        """
        Return the last_name plus the first_name (plus the second_name), with a space in between.
        """
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.second_name)
        return full_name.strip()
    
    def get_full_name_initials(self):
        """
        Return the last_name plus the first_name (plus the second_name), with a space in between. (first_name and second_name is initials)
        """
        initials = ''
        initials += self.first_name[0] + '.' if  self.first_name else ''
        initials += self.second_name[0] + '.' if  self.second_name else ''
        full_name_initials = '%s %s' % (self.last_name, initials)
        return full_name_initials.strip()

    class Meta(AbstractUser.Meta):
        pass