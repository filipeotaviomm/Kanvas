from rest_framework.permissions import BasePermission, SAFE_METHODS
from contents.models import Content


class IsSuperuser(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class IsAccountEnrolledInCourseOrIsSuperuser(BasePermission):
    def has_object_permission(self, request, view, obj: Content) -> bool:
        return (
            request.method in SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )
