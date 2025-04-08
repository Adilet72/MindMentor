from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Доступ только для админов"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsMentor(BasePermission):
    """Доступ только для менторов"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'mentor'


class IsUser(BasePermission):
    """Доступ только для обычных пользователей"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'
