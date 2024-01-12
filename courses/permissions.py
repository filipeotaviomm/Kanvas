from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperuserOrAuthenticated(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return request.user.is_superuser


class IsSuperuser(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser
