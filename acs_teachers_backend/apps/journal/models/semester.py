"""
semester.py file
Semester model class
"""
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class Semester(models.Model):
	date_start = models.DateField(default=datetime.date.today, verbose_name=_('date education start'))
	date_end = models.DateField(default=datetime.date.today, verbose_name=_('date education end'))
	slug = models.CharField(max_length=200, blank=True, unique=True, verbose_name=_('slug'), help_text=_('must use english letters, and dash signs for spaces (autogenerate)'))

	class Meta:
		verbose_name = _('semester')
		verbose_name_plural = _('semesters')

	def save(self, *args, **kwargs):
		"""
		Save the current instance. 
		On creation (id is null) generate slug if not exist
		"""
		if not self.id and not self.slug:
			self.slug = "{start_date}-{end_date}".format(
				start_date = self.date_start.strftime("%m-%Y"), 
				end_date = self.date_end.strftime("%m-%Y")
			)
		super().save(*args, **kwargs)

	def __str__(self):
		return "%s %s" % (self.date_start, self.date_end)