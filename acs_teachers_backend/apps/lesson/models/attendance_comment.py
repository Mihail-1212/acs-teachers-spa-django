"""
attendance_comment.py file
AttendanceComment model class
"""
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from .attendance import Attendance

class AttendanceComment(models.Model):
    related_name = 'attendance_comments'
    # folder name for subdirectory media (model_name + 'media')
    media_upload_path = 'attendance_comment_media'

    message = models.TextField(max_length=500, verbose_name=_('message'))
    pub_date = models.DateTimeField(default=timezone.now, verbose_name=_('publish date'))
    is_checked = models.BooleanField(default=False, verbose_name=_('is read'))

    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, verbose_name=_('attendance'),
                                 related_name=related_name)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('author'),
                                 related_name=related_name)

    media = models.FileField(upload_to=media_upload_path, verbose_name=_('file'))

    class Meta:
        verbose_name = _('attendance comment')
        verbose_name_plural = _('attendance comments')
        ordering = ['pub_date']

    def __str__(self):
        return self.message