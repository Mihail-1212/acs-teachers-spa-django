"""
journal.py file
Journal model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
# from month.models import MonthField

from .semester import Semester
from .discipline import Discipline
from .student_group import StudentGroup
from teacher.models.teacher import Teacher

class Journal(models.Model):
	related_name = "journals"

	name = models.CharField(max_length=200, unique=False, verbose_name=_('name'))
	slug = models.CharField(max_length=200, unique=True, verbose_name=_('slug'))

	semester = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name=_('semester'), related_name=related_name)
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name=_('discipline'), related_name=related_name)
	student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name=_('student group'), related_name=related_name)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_('teacher'), related_name=related_name)

	class Meta:
		verbose_name = _('journal')
		verbose_name_plural = _('journals')