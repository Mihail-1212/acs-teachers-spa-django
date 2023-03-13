"""
student_group.py file
StudentGroup model class
"""
import cyrtranslit

from django.db import models
from django.utils.translation import gettext_lazy as _

from .edu_organization import EduOrganization
from .speciality import Speciality


class StudentGroup(models.Model):
	related_name = 'student_groups'

	name = models.CharField(max_length=200, unique=False, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=False, verbose_name=_('abbreviation'))
	slug = models.CharField(max_length=200, blank=True, unique=True, verbose_name=_('slug'), help_text=_('must use english letters, and dash signs for spaces (autogenerate)'))
	date_start_edu = models.DateField(verbose_name=_('date education start'))
	date_end_edu = models.DateField(verbose_name=_('date education end'))
	is_commercial = models.BooleanField(default=False, verbose_name=_('is commercial'))

	speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name=_('speciality'), related_name=related_name)
	edu_organization = models.ForeignKey(EduOrganization, on_delete=models.CASCADE, verbose_name=_('education organization'), related_name=related_name)

	class Meta:
		verbose_name = _('student group')
		verbose_name_plural = _('student groups')

	def save(self, *args, **kwargs):
		"""
		Save the current instance. 
		On creation (id is null) generate slug if not exist
		"""
		if not self.id and not self.slug:
			self.slug = "{abbr}-{edu_org}".format(
				abbr = cyrtranslit.to_latin(self.abbr.replace(" ", "")), 
				edu_org = cyrtranslit.to_latin(self.edu_organization.abbr.replace(" ", ""))
			)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.abbr

	# def __str__(self):
	# 	return "%s %s" % (self.date_start, self.date_end)