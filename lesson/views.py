from rest_framework.viewsets import ModelViewSet
from .models import Lesson
from rest_framework import permissions
from .serializers import LessonListSerializer, LessonDetailSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from lesson_impressions.serializers import LikeSerializer, DislikeSerializer
from rest_framework.response import Response
from lesson_impressions.models import Like, Dislike
from question.serializers import QuestionSerializer, CreateQuestionSerializer


class StandardResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'lesson'


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    pagination_class = StandardResultPagination

    def get_serializer_class(self):
        if self.action in ['list']:
            return LessonListSerializer
        return LessonDetailSerializer

    def get_permissions(self):
        if self.action in ['list']:
            return permissions.IsAuthenticatedOrReadOnly(),
        if self.action in ['destroy', 'update', 'create', 'partial_update']:
            return permissions.IsAdminUser(),
        return permissions.IsAuthenticated(),

    @action(methods=['GET', 'POST'], detail=True)
    def likes(self, request, pk):
        lesson = self.get_object()
        user = request.user
        if request.method == 'GET':
            likes = lesson.likes.all()
            serializer = LikeSerializer(instance=likes, many=True)
            return Response(serializer.data, status=200)
        elif request.method == 'POST':
            if user.likes.filter(lesson=lesson).exists():
                user.likes.filter(lesson=lesson).delete()
                return Response('Like was removed', status=204)
            Like.objects.create(owner=user, lesson=lesson)
            return Response('Like was added', status=201)

    @action(methods=['GET', 'POST'], detail=True)
    def dislikes(self, request, pk):
        lesson = self.get_object()
        user = request.user
        if request.method == 'GET':
            dislikes = lesson.dislikes.all()
            serializer = DislikeSerializer(instance=dislikes, many=True)
            return Response(serializer.data, status=200)
        elif request.method == 'POST':
            if user.dislikes.filter(lesson=lesson).exists():
                user.dislikes.filter(lesson=lesson).delete()
                return Response('Dislike was removed', status=204)
            Dislike.objects.create(owner=user, lesson=lesson)
            return Response('Dislike was added', status=201)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def questions(self, request, pk):
        lesson = self.get_object()
        user = request.user
        if self.request.method == 'GET':
            questions = lesson.questions.all()
            serializer = QuestionSerializer(instance=questions, many=True, context={'owner': user})
            return Response(serializer.data, status=200)
        elif self.request.method == 'POST':
            if lesson.questions.all().exists():
                return Response('This lesson already has a question', status=400)
            serializer = CreateQuestionSerializer(data=request.data, context={'lesson': lesson})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('Question created!', status=201)
        elif self.request.method == 'DELETE':
            if not lesson.questions.all().exists():
                return Response('This lesson doesnt have any questions!', status=400)
            lesson.questions.get(lesson=lesson).delete()
            return Response('Question deleted', status=204)
