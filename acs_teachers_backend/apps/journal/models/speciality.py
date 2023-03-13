"""
speciality.py file
Speciality model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .edu_organization import EduOrganization

class Speciality(models.Model):
	related_name = 'specialities'

	name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=True, verbose_name=_('abbreviation'))

	edu_organizations = models.ManyToManyField(EduOrganization, verbose_name=_('education organizations'), related_name=related_name)

	class Meta:
		verbose_name =  _('speciality')
		verbose_name_plural =  _('specialities')

	def __str__(self):
		return self.name