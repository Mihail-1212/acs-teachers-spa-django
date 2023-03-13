from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LessonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson'
    verbose_name = _('Lessons and attendance')
