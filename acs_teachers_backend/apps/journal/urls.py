from django.urls import path, include
from rest_framework import routers
from django.views.generic import RedirectView
from django.urls import path

from . import api


router = routers.DefaultRouter()

router.register(r'edu-organizations', api.EduOrganizationViewSet, basename="edu-organization")
router.register(r'specialities', api.SpecialityViewSet, basename="speciality")
router.register(r'disciplines', api.DisciplineViewSet, basename="discipline")


urlpatterns = [
    path('', include(router.urls)),
]

