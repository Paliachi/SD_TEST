from django.contrib import admin

from .models import Student, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_description', 'professor')
    list_filter = ('course_name',)

