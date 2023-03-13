"""
attendance.py file
Attendance  model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .lesson import Lesson
from student.models import Student


class Attendance(models.Model):

    class AttendanceGrade(models.TextChoices):
        PRESENT = '+', _('Present')
        ABSENT = _('none'), _('Absent')
        ABSENT_REASON = _('none (reas.)'), _("Absent (for a good reason)")
        NOT_MARKED = '?', _('Not marked')

    related_name = "attendance"

    grade = models.CharField(max_length=50, blank=False, choices=AttendanceGrade.choices, default=AttendanceGrade.NOT_MARKED,
                             verbose_name='Оценка посещаемости')

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('lesson'),
                                 related_name=related_name)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('student'),
                                related_name=related_name)

    class Meta:
        verbose_name = _('attendance')
        verbose_name_plural = _('attendance')
        constraints = [
            models.UniqueConstraint(fields=['lesson', 'student'], name='unique attendance grade field')
        ]