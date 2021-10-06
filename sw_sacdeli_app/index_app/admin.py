from django.contrib import admin

from .models import Student, Course, EnrolledCourse


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(EnrolledCourse)
