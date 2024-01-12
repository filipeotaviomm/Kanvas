from courses.models import Course
from courses.serializers import CourseSerializer, CourseStudentsSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.permissions import IsSuperuserOrAuthenticated, IsSuperuser
from rest_framework.generics import get_object_or_404


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrAuthenticated]

    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()

        return Course.objects.filter(students=self.request.user)


class CourseIdView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrAuthenticated]

    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.filter(id=self.kwargs.get("course_id"))

        return Course.objects.filter(students=self.request.user)


class CourseStudentView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Course.objects.all()
    serializer_class = CourseStudentsSerializer
    lookup_url_kwarg = "course_id"
