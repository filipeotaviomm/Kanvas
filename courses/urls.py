from django.urls import path
from courses.views import CourseView, CourseIdView, CourseStudentView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<course_id>/", CourseIdView.as_view()),
    path("courses/<course_id>/students/", CourseStudentView.as_view()),
]
