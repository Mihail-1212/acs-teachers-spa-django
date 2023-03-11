from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TeacherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teacher'
    verbose_name = _('teacher')
