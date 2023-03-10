from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'
    verbose_name = _('Students application')
