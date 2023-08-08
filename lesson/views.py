from rest_framework.viewsets import ModelViewSet
from .models import Lesson
from rest_framework import generics, permissions
from .serializers import LessonListSerializer, LessonDetailSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = permissions.IsAuthenticated,
    pagination_class = StandardResultPagination

    def get_serializer_class(self):
        if self.action in ['list']:
            return LessonListSerializer
        return LessonDetailSerializer

