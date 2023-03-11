"""
student.py file
Student model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from journal.models import StudentGroup

class Student(models.Model):
	related_name = 'students'

	option_num = models.IntegerField(blank=True, verbose_name=_('student option number in group'))

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'), related_name=related_name)
	student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name=_('student group'), related_name=related_name)

	class Meta:
		verbose_name = _('student')
		verbose_name_plural = _('students')
        
	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.user.get_full_name() 