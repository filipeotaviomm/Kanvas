from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from courses.models import Course
from students_courses.serializers import StudentCourseSerializer
from accounts.models import Account


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        read_only_fields = [
            "id",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            },
        }


class CourseStudentsSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["id", "name", "students_courses"]

    def update(self, instance: Course, validated_data: dict):
        email_found = []
        email_not_found = []
        for sent_email in validated_data["students_courses"]:
            account_found = Account.objects.filter(
                email=sent_email["student"]["email"]
            ).first()
            print(account_found, "************* account_found")
            print(sent_email["student"]["email"], "------------ sent_email")
            print(validated_data["students_courses"])
            if account_found:
                email_found.append(account_found)
            else:
                email_not_found.append(sent_email["student"]["email"])
        if email_not_found:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(email_not_found)}."
                }
            )
        instance.students.add(*email_found)
        return instance
