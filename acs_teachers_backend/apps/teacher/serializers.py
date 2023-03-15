from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models


class UserTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username', 'first_name', 'last_name', 'second_name', 'email', 'is_active',
        ]


class TeacherSerializer(serializers.ModelSerializer):
    user = UserTeacherSerializer(read_only=True, many=False)

    class Meta:
        model = models.Teacher
        fields = '__all__'
