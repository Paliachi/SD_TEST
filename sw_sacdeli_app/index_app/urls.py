from rest_framework import routers

from django.urls import path, include

# from .views import StudentViewSet, CourseViewSet
from .views import StudentViewSet

# router = routers.DefaultRouter()
# router.register('students', StudentViewSet)
# router.register('courses', CourseViewSet)

urlpatterns = [
    path('students/', StudentViewSet.as_view({'get': 'list'})),
    path('create-student/', StudentViewSet.as_view({'post': 'create'})),
    path('change-student/<int:pk>', StudentViewSet.as_view({'put': 'update'})),
]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-students/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# urlpatterns = [
#     path('students/', student_list, name='students'),
#     path('student-detail/<int:pk>', student_detail, name='student_detail'),
#
# ]
