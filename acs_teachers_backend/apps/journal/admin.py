from django.contrib import admin
# from django.conf import settings

from .models import *



class SemesterAdmin(admin.ModelAdmin):
	list_display = ('date_start', 'date_end', 'slug', )
	readonly_fields = ('slug',)

class StudentGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbr', 'date_start_edu', 'is_commercial', 'slug')

class JournalAdmin(admin.ModelAdmin):
	list_display = ('name', 'semester', 'discipline', 'student_group', 'teacher', 'slug')


admin.site.register(EduOrganization)
admin.site.register(Speciality)
admin.site.register(StudentGroup, StudentGroupAdmin)

admin.site.register(Semester, SemesterAdmin)
admin.site.register(Discipline)
admin.site.register(Journal, JournalAdmin)

# if settings.DEBUG:
# 	admin.site.register(Journal)
