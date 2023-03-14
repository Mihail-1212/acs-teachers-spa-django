from enum import unique
from strenum import StrEnum

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (
    IsAdminUser
)
from django.utils.translation import gettext_lazy as _

from . import serializers
from . import models


@unique
class ApiParams(StrEnum):
    """
    Api enum set params for viewset classes
    """
    EDU_ORGANIZATION_ID = "edu_organization_id"
    SPECIALITY_ID = "speciality_id"


class EduOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.EduOrganization.objects.all()
    serializer_class = serializers.EduOrganizationSerializer
    lookup_field = 'id'


class SpecialityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.SpecialitySerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        Get the list of items for this view
        """
        # Getting queryset
        queryset = models.Speciality.objects.all()

        # Get education organization id from URL GET params
        edu_organization_id = self.request.query_params.get(ApiParams.EDU_ORGANIZATION_ID)
        if edu_organization_id is not None:
            if not edu_organization_id.isnumeric():
                raise ValidationError(_("Education organization id should be a number value"))
            queryset = queryset.filter(edu_organizations__id=edu_organization_id)

        return queryset


class DisciplineViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DisciplineSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        """
        Get the list of items for this view
        """
        # Getting queryset
        queryset = models.Discipline.objects.all()

        # Get speciality id from URL GET params
        speciality_id = self.request.query_params.get(ApiParams.SPECIALITY_ID)
        if speciality_id is not None:
            if not speciality_id.isnumeric():
                raise ValidationError(_("Speciality id should be a number value"))
            queryset = queryset.filter(specialities__id=speciality_id)

        # Get education organization id from URL GET params
        edu_organization_id = self.request.query_params.get(ApiParams.EDU_ORGANIZATION_ID)
        if edu_organization_id is not None:
            if not edu_organization_id.isnumeric():
                raise ValidationError(_("Education organization id should be a number value"))
            queryset = queryset.filter(specialities__edu_organizations__id=edu_organization_id)

        return queryset
