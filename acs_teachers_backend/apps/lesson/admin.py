from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *

class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date', 'type', 'get_teacher', 'get_student_group', 'get_discipline')

    @admin.display(ordering='journal__teacher', description=_('Teacher'))
    def get_teacher(self, obj):
        return obj.journal.teacher

    @admin.display(ordering='journal__student_group', description=_('student group'))
    def get_student_group(self, obj):
        return obj.journal.student_group

    @admin.display(ordering='journal__discipline', description=_('discipline'))
    def get_discipline(self, obj):
        return obj.journal.discipline


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('grade', 'lesson', 'student', 'id')

class AttendanceCommentAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'author', 'is_checked', 'id')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceComment, AttendanceCommentAdmin)


