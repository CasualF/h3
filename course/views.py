from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import CourseDetailSerializer, SubjectSerializer, CourseListSerializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from course_impressions.serializers import ReviewSerializer
from rest_framework.response import Response
from .models import Course, Subject


class StandardResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        print(super().get_queryset())
        return super().get_queryset()

    def get_permissions(self):
        if self.action in ['destroy', 'create', 'update', 'partial_update']:
            return IsAdminUser(),
        return IsAuthenticatedOrReadOnly(),


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = StandardResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'description')
    filterset_fields = ('title', 'description', 'subject__title')
    serializer_class = CourseDetailSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'create', 'update', 'partial_update']:
            return IsAdminUser(),
        return IsAuthenticatedOrReadOnly(),

    def get_serializer_class(self):
        if self.action in ['list']:
            return CourseListSerializer
        return CourseDetailSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def reviews(self, request, pk):
        course = self.get_object()
        user = request.user
        if request.method == 'GET':
            reviews = course.reviews.all()
            serializer = ReviewSerializer(instance=reviews, many=True)
            return Response(serializer.data, status=200)

        elif request.method == 'POST':
            review = course.reviews.filter(owner=user)
            if not review.exists():
                serializer = ReviewSerializer(data=request.data, context={'course': course, 'owner': user})
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response('You can only have 1 review', status=400)

        elif request.method == 'DELETE':
            review = course.reviews.filter(owner=user)
            if review.exists():
                review.delete()
                return Response('Successfully deleted', status=204)
        return Response('Not found', status=404)