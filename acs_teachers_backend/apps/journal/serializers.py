from rest_framework import serializers

from . import models
from teacher.serializers import TeacherSerializer


class EduOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer to show for retrieve func
    """
    class Meta:
        model = models.EduOrganization
        fields = '__all__'
        lookup_field = 'id'
        extra_kwargs = {
            'url': {
                'lookup_field': 'id',
                'view_name': 'edu-organization-detail',
            }
        }


class EduOrganizationUrlSerializer(serializers.HyperlinkedModelSerializer):
    """
    Education organization serializer contain url only
    """
    class Meta:
        model = models.EduOrganization
        fields = ['url']
        lookup_field = 'id'
        extra_kwargs = {
            'url': {
                'lookup_field': 'id',
                'view_name': 'edu-organization-detail',
            }
        }


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    edu_organizations = EduOrganizationUrlSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = models.Speciality
        fields = '__all__'
        depth = 0
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    specialities = SpecialitySerializer(read_only=True, many=True)

    class Meta:
        model = models.Discipline
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Semester
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class StudentGroupSerializer(serializers.HyperlinkedModelSerializer):
    speciality = SpecialitySerializer(read_only=True, many=False)
    edu_organization = EduOrganizationSerializer(read_only=True, many=False)

    class Meta:
        model = models.StudentGroup
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
                'view_name': 'student-group-detail',
            }
        }


class JournalSerializer(serializers.HyperlinkedModelSerializer):
    discipline = DisciplineSerializer(read_only=True, many=False)
    semester = SemesterSerializer(read_only=True, many=False)
    student_group = StudentGroupSerializer(read_only=True, many=False)
    teacher = TeacherSerializer(read_only=True, many=False)

    class Meta:
        model = models.Journal
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug',
            }
        }