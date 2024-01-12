from rest_framework import serializers
from students_courses.models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    student_id = serializers.SerializerMethodField()
    student_username = serializers.SerializerMethodField()
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]
        read_only_fields = ["id", "status", "student_id", "student_username"]

    def get_student_id(self, obj: StudentCourse):
        return obj.student.id

    def get_student_username(self, obj: StudentCourse):
        return obj.student.username
