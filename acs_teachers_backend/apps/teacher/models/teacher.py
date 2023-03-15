"""
teacher.py file
Teacher model class
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Teacher(models.Model):
    related_name = 'teachers'
    related_name_single = 'teacher'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'),
                                related_name=related_name_single)

    class Meta:
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.get_full_name()
