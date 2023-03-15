from django.urls import path, include
from rest_framework import routers

from . import api


router = routers.DefaultRouter()

router.register(r'edu-organizations', api.EduOrganizationViewSet, basename="edu-organization")
router.register(r'specialities', api.SpecialityViewSet, basename="speciality")
router.register(r'disciplines', api.DisciplineViewSet, basename="discipline")

router.register(r'semesters', api.SemesterViewSet, basename="semester")

router.register(r'student-groups', api.StudentGroupViewSet, basename="student-group")

router.register(r'journals', api.JournalViewSet, basename="journal")


urlpatterns = [
    path('', include(router.urls)),
]

