"""
semester.py file
Semester model class
"""
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from month.models import MonthField

class Semester(models.Model):
	date_start = models.DateField(default=datetime.date.today, verbose_name=_('date education start'))
	date_end = models.DateField(default=datetime.date.today, verbose_name=_('date education end'))
	slug = models.CharField(max_length=200, unique=True, verbose_name=_('slug'))

	class Meta:
		verbose_name = _('semester')
		verbose_name_plural = _('semesters')