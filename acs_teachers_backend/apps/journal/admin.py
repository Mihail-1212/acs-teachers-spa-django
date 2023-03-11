from django.contrib import admin
# from django.conf import settings

from .models import *

# Register your models here.


admin.site.register(EduOrganization)
admin.site.register(Speciality)
admin.site.register(StudentGroup)

admin.site.register(Semester)
admin.site.register(Discipline)
admin.site.register(Journal)

# if settings.DEBUG:
# 	admin.site.register(Journal)
