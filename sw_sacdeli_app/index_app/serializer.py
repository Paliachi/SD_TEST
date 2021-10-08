from rest_framework import serializers

from .models import Student, Course, EnrolledCourse


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'professor']


class EnrolledCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledCourse
        # depth = 1
        fields = ['id', 'student', 'course']


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     phone = serializers.CharField(max_length=9)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.save()
#         return instance

