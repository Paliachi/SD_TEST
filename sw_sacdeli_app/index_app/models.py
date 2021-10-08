from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(max_length=255)
    professor = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=9)
    courses = models.ManyToManyField(Course, related_name='student')

    def __str__(self):
        return self.name
