"""
lesson.py file
Lesson model class
"""
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from journal.models import Journal


class Lesson(models.Model):

    class LessonType(models.TextChoices):
        """
        TextChoices for lesson.type CharField
        """
        LECTURE = _('lec.'), _('Lecture')
        LABORATORY_WORK = _('LW'), _('Laboratory work')
        PRACTICAL_WORK = _('PW'), _('Practical work')

    related_name = "lessons"

    name = models.CharField(max_length=200, unique=False, verbose_name=_('name'))
    date = models.DateField(default=datetime.date.today, verbose_name=_('lesson date'))
    number = models.IntegerField(blank=True, verbose_name=_('number of lesson'))
    theme = models.TextField(max_length=200, blank=True, verbose_name=_('theme of lesson'))
    type = models.CharField(max_length=50, choices=LessonType.choices, default=LessonType.LECTURE,
                            verbose_name=_('type of lesson'))

    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, verbose_name=_('journal'),
                                 related_name=related_name)

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')

    def __str__(self):
        return "%s (%s)" % (self.name, self.number)

    # TODO: При создании создание экзмепляров Attendance для всех студентов в группе journal.student_group