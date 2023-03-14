from rest_framework import serializers

from . import models


class EduOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EduOrganization
        fields = '__all__'

        # view_name = 'edu-organization'

        lookup_field = 'id'
        extra_kwargs = {
            'url': {
                'lookup_field': 'id',
                'view_name': 'edu-organization-detail',
            }
        }


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    edu_organizations = EduOrganizationSerializer(read_only=True, many=True)

    class Meta:
        model = models.Speciality
        fields = '__all__'
        depth = 1
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
