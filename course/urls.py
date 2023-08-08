from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, SubjectViewSet

router = DefaultRouter()

router.register('courses', CourseViewSet)
router.register('subjects', SubjectViewSet)


urlpatterns = [
    path('', include(router.urls))
]
