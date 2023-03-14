from rest_framework import viewsets
from rest_framework.permissions import (
    IsAdminUser
)

from . import serializers
from . import models


class EduOrganizationViewSet(viewsets.ModelViewSet):
    queryset = models.EduOrganization.objects.all()
    serializer_class = serializers.EduOrganizationSerializer
    lookup_field = 'id'


class SpecialityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Speciality.objects.all()
    serializer_class = serializers.SpecialitySerializer
    lookup_field = 'id'


class DisciplineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Discipline.objects.all()
    serializer_class = serializers.DisciplineSerializer
    lookup_field = 'slug'


