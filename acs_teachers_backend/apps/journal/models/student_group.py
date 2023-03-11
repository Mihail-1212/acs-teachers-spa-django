"""
student_group.py file
StudentGroup model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from month.models import MonthField

from .edu_organization import EduOrganization
from .speciality import Speciality


class StudentGroup(models.Model):
	related_name = 'student_groups'

	name = models.CharField(max_length=200, unique=False, verbose_name=_('name'))
	abbr = models.CharField(max_length=50, unique=False, verbose_name=_('abbreviation'))
	slug = models.CharField(max_length=200, unique=True, verbose_name=_('slug'))
	date_start_edu = MonthField(verbose_name=_('date education start'))
	date_end_enu = MonthField(verbose_name=_('date education end'))
	is_commercial = models.BooleanField(default=False, verbose_name=_('is commercial'))

	speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name=_('speciality'), related_name=related_name)
	edu_organization = models.ForeignKey(EduOrganization, on_delete=models.CASCADE, verbose_name=_('education organization'), related_name=related_name)

	class Meta:
		verbose_name = _('student group')
		verbose_name_plural = _('student groups')