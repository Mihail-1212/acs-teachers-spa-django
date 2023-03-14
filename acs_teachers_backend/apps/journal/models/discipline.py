"""
discipline.py file
Discipline model class
"""
import cyrtranslit

from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from .speciality import Speciality


class Discipline(models.Model):
	related_name = "disciplines"

	name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=True, verbose_name=_('abbreviation'))
	slug = models.CharField(max_length=200, blank=True, unique=True, verbose_name=_('slug'), help_text=_('must use english letters, and dash signs for spaces (autogenerate)'))

	specialities = models.ManyToManyField(Speciality, verbose_name=_('specialities'), related_name=related_name)

	class Meta:
		verbose_name =  _('discipline')
		verbose_name_plural =  _('disciplines')

	def save(self, *args, **kwargs):
		"""
		Save the current instance. 
		On creation (id is null) generate slug if not exist
		"""
		if not self.id and not self.slug:
			self.slug = "{abbr}".format(
				abbr = cyrtranslit.to_latin(self.abbr.replace(" ", "")),
			)
		super().save(*args, **kwargs)

	# def get_absolute_url(self):
	# 	return ""

	def __str__(self):
		return "%s (%s)" % (self.abbr, self.name)