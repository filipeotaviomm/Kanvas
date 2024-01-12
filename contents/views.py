from contents.models import Content
from courses.models import Course
from contents.serializers import ContentSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from contents.permissions import (
    IsAccountEnrolledInCourseOrIsSuperuser,
    IsSuperuser,
)


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        found_course = get_object_or_404(Course, id=self.kwargs.get("course_id"))
        return serializer.save(course=found_course)


class ContentIdView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountEnrolledInCourseOrIsSuperuser]

    serializer_class = ContentSerializer

    def get_object(self):
        content = Content.objects.filter(id=self.kwargs["content_id"])
        course = Course.objects.filter(id=self.kwargs["course_id"])
        if not content:
            raise NotFound("content not found.")
        if not course:
            raise NotFound("course not found.")
        self.check_object_permissions(self.request, content.first())
        return content.first()
