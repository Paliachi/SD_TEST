from rest_framework import routers

from django.urls import path, include

from .views import StudentViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)


urlpatterns = router.urls

# urlpatterns = [
#     # path('students', StudentViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'}), name='students'),
#     # path('create-student/', StudentViewSet.as_view({'put': 'create'}), name='create_student'),
#     # path('change-student/<int:pk>', StudentViewSet.as_view({}), name='change_student'),
#
#
#     path('courses/', CourseViewSet.as_view({'get': 'list'}), name='courses'),
#     path('create-course/', CourseViewSet.as_view({'post': 'create'}), name='create_course'),
#
#
# ]

