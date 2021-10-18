from django.test import SimpleTestCase
from django.urls import reverse, resolve

from index_app.models import Course, Student
from index_app.views import StudentViewSet, CourseViewSet


class StudentUrlsTest(SimpleTestCase):
    def test_students_list(self):
        resolver = resolve("/api/students/")
        self.assertEqual(resolver.func.cls, StudentViewSet)


