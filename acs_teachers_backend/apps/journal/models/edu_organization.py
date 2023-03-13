"""
edu_organization.py file
EducationOrganization model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class EduOrganization(models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=True, verbose_name=_('abbreviation'))

	class Meta:
		verbose_name = _('education organization')
		verbose_name_plural = _('education organizations')

	def __str__(self):
		return self.abbr
	