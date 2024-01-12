from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from courses.models import Course


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False, null=True)

    my_courses = models.ManyToManyField(
        Course, through="students_courses.StudentCourse", related_name="students"
    )
