"""
Provides a set of pluggable permission policies.
"""
from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    """
    Allows access only to student users
    """

    def has_permission(self, request, view):
        return hasattr(request.user, 'student') and request.user.student is not None
