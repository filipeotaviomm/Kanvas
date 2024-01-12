from django.db import models
from accounts.models import Account
from courses.models import Course
import uuid


class StudentCourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.PENDING,
        null=True,
        max_length=100,
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students_courses"
    )
    student = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="students_courses"
    )
