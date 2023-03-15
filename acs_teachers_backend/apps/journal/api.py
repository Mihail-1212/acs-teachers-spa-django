from enum import unique
from strenum import StrEnum

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import (
    IsAdminUser
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import gettext_lazy as _

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

    @action(detail=False, permission_classes=[(IsAdminUser | IsStudent)])
    def get_journal_list_student(self, request):
        """
        Get journal list for student user
        /journals/get_journal_list_student/?student=<id>
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
            permission_classes = [(IsAdminUser | IsTeacher | IsStudent)]     # TODO: add IsStudent
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


