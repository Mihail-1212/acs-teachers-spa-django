"""
Speciality.py file
Speciality model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Speciality(models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=True, verbose_name=_('abbreviation'))

	class Meta:
		verbose_name =  _('speciality')
		verbose_name_plural =  _('specialities')