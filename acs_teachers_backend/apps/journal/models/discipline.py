"""
discipline.py file
Discipline model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .speciality import Speciality


class Discipline(models.Model):
	related_name = "disciplines"

	name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=True, verbose_name=_('abbreviation'))
	slug = models.CharField(max_length=200, unique=True, verbose_name=_('slug'))

	specialities = models.ManyToManyField(Speciality, verbose_name=_('specialities'), related_name=related_name)

	class Meta:
		verbose_name =  _('discipline')
		verbose_name_plural =  _('disciplines')