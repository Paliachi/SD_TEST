from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Student, Course, EnrolledCourse
from .serializer import StudentSerializer, CourseSerializer, EnrolledCourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        enrolled_courses_queryset = EnrolledCourse.objects.all()

        serializer = StudentSerializer(queryset, many=True)
        enrolled_courses_serializer = EnrolledCourseSerializer(enrolled_courses_queryset, many=True)
        st_ser = serializer.data.copy()
        cr_ser = enrolled_courses_serializer.data.copy()

        for st in st_ser:
            st['course(s)'] = [cr['course'] for cr in cr_ser if cr['student']['id'] == st['id']]
        print(st_ser)

        return Response(st_ser)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)


class EnrolledCourseViewSet(viewsets.ModelViewSet):
    queryset = EnrolledCourse.objects.all()
    serializer_class = EnrolledCourseSerializer
    permission_classes = (permissions.AllowAny,)


# @csrf_exempt
# def student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def student_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(student, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         student.delete()
#         return HttpResponse(status=204)

