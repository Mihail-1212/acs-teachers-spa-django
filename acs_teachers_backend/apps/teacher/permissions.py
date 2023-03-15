"""
Provides a set of pluggable permission policies.
"""
from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    """
    Allows access only to teacher users
    """

    def has_permission(self, request, view):
        return hasattr(request.user, 'teacher') and request.user.teacher is not None

    # def has_object_permission(self, request, view, obj):
    #     if obj.teacher is not None and request.user.teacher is not None:
    #         if obj.teacher.id == request.user.teacher.id:
    #             return False
    #     return True

