from enum import unique
from strenum import StrEnum

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import (
    IsAdminUser
)
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from . import serializers
from . import models
from teacher.permissions import IsTeacher
from student.permissions import IsStudent


@unique
class ApiParams(StrEnum):
    """
    Api enum set params for viewset classes
    """
    EDU_ORGANIZATION_ID = "edu_organization_id"
    SPECIALITY_ID = "speciality_id"
    TEACHER_ID = "teacher_id"
    STUDENT_ID = "student_id"


class SwaggerApiParams():
    """
    Swagger api enum set params for viewset classes
    """
    EDU_ORGANIZATION_ID_SPECIALITY = openapi.Parameter(ApiParams.EDU_ORGANIZATION_ID, openapi.IN_QUERY,
                                                       required=False,
                                                       description=_("Education organization id GET param"),
                                                       type=openapi.TYPE_INTEGER)

    SPECIALITY_ID_DISCIPLINE = openapi.Parameter(ApiParams.SPECIALITY_ID, openapi.IN_QUERY,
                                                 description=_("Speciality id GET param"),
                                                 required=False,
                                                 type=openapi.TYPE_INTEGER)

    TEACHER_ID_JOURNAL = openapi.Parameter(ApiParams.TEACHER_ID, openapi.IN_QUERY,
                                           description=_("Teacher id GET param"),
                                           required=True,
                                           type=openapi.TYPE_INTEGER)

    STUDENT_ID_JOURNAL = openapi.Parameter(ApiParams.STUDENT_ID, openapi.IN_QUERY,
                                           description=_("Student id GET param"),
                                           required=True,
                                           type=openapi.TYPE_INTEGER)


class EduOrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.EduOrganization.objects.all()
    serializer_class = serializers.EduOrganizationSerializer
    lookup_field = 'id'


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description=_("Get full list of specialities OR get list by education_organization_id param"),
    manual_parameters=[SwaggerApiParams.EDU_ORGANIZATION_ID_SPECIALITY],
))
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
        if edu_organization_id is not None and self.action == 'list':
            if not edu_organization_id.isnumeric():
                raise ValidationError(_("Education organization id should be a number value"))
            queryset = queryset.filter(edu_organizations__id=edu_organization_id)

        return queryset


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description=_("Get full list of disciplines OR get list "
                            "by speciality_id param OR get list by edu_organization_id"),
    manual_parameters=[SwaggerApiParams.SPECIALITY_ID_DISCIPLINE, SwaggerApiParams.EDU_ORGANIZATION_ID_SPECIALITY],
))
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
        if speciality_id is not None and self.action == 'list':
            if not speciality_id.isnumeric():
                raise ValidationError(_("Speciality id should be a number value"))
            queryset = queryset.filter(specialities__id=speciality_id)

        # Get education organization id from URL GET params
        edu_organization_id = self.request.query_params.get(ApiParams.EDU_ORGANIZATION_ID)
        if edu_organization_id is not None and self.action == 'list':
            if not edu_organization_id.isnumeric():
                raise ValidationError(_("Education organization id should be a number value"))
            queryset = queryset.filter(specialities__edu_organizations__id=edu_organization_id)

        return queryset


class SemesterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Semester.objects.all()
    serializer_class = serializers.SemesterSerializer
    lookup_field = 'slug'


class StudentGroupViewSet(viewsets.ReadOnlyModelViewSet):
    speciality = SpecialityViewSet()
    queryset = models.StudentGroup.objects.all()
    serializer_class = serializers.StudentGroupSerializer
    lookup_field = 'slug'


class JournalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer
    lookup_field = 'slug'

    @swagger_auto_schema(method='get', manual_parameters=[SwaggerApiParams.TEACHER_ID_JOURNAL])
    @action(detail=False, permission_classes=[(IsAdminUser | IsTeacher)])
    def get_journal_list_teacher(self, request):
        """
        Get journal list for teacher user
        /journals/get_journal_list_teacher/?teacher_id=<id>
        """
        journal_list = self.get_queryset()

        teacher_id = request.query_params.get(ApiParams.TEACHER_ID)

        if teacher_id is None or not teacher_id.isnumeric():
            raise ValidationError(_("Teacher id is required and should be a number value"))

        if not request.user.is_staff and not teacher_id == request.user.teacher.id:
            raise PermissionDenied(_("User has no access to another teacher journals"))

        journal_list = journal_list.filter(teacher__id=teacher_id)

        serializer = self.get_serializer(journal_list, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(method='get', manual_parameters=[SwaggerApiParams.STUDENT_ID_JOURNAL])
    @action(detail=False, permission_classes=[(IsAdminUser | IsStudent)])
    def get_journal_list_student(self, request):
        """
        Get journal list for student user
        /journals/get_journal_list_student/?student_id=<id>
        """
        journal_list = self.get_queryset()

        student_id = request.query_params.get(ApiParams.STUDENT_ID)

        if student_id is None or not student_id.isnumeric():
            raise ValidationError(_("Student id is required and should be a number value"))

        if not request.user.is_staff and not student_id == request.user.student.id:
            raise PermissionDenied(_("User has no access to another student journals"))

        journal_list = journal_list.filter(student_group__students__id=student_id)

        serializer = self.get_serializer(journal_list, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [(IsAdminUser | IsTeacher | IsStudent)]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


