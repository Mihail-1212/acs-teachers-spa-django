"""
journal.py file
Journal model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .semester import Semester
from .discipline import Discipline
from .student_group import StudentGroup
from teacher.models.teacher import Teacher

class Journal(models.Model):
	related_name = "journals"

	name = models.CharField(max_length=200, unique=False, verbose_name=_('name'))
	slug = models.CharField(max_length=200, blank=True, unique=True, verbose_name=_('slug'), help_text=_('must use '
																										 'english '
																										 'letters, '
																										 'and dash '
																										 'signs for '
																										 'spaces ('
																										 'autogenerate)'))

	semester = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name=_('semester'), related_name=related_name)
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name=_('discipline'), related_name=related_name)
	student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name=_('student group'), related_name=related_name)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_('teacher'), related_name=related_name)

	class Meta:
		verbose_name = _('journal')
		verbose_name_plural = _('journals')

	def save(self, *args, **kwargs):
		"""
		Save the current instance. 
		On creation (id is null) generate slug if not exist
		"""
		if not self.id and not self.slug:
			self.slug = "{semester}-{discipline}-{student_group}-{teacher}".format(
    			semester = self.semester.slug,
				discipline = self.discipline.slug,
				student_group = self.student_group.slug,
            	teacher = self.teacher.user.username.replace(" ", "")
			)
		super().save(*args, **kwargs)

	def __str__(self):
		return "%s (%s)" % (self.name, self.slug)