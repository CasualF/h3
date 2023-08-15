from rest_framework import serializers
from django.db.models import Avg
from .models import Course, Subject
from lesson.serializers import LessonListSerializer, LessonDetailSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(CourseDetailSerializer, self).to_representation(instance)
        representation['lesson_count'] = instance.lessons.count()
        representation['lessons'] = LessonListSerializer(instance=instance.lessons.all().order_by('created_at'),
                                                         many=True).data
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        representation['favorite_count'] = instance.favorites.count()
        try:
            user = self.context['request'].user
            if user.is_authenticated:
                representation['is_favorite'] = self.is_favorite(instance, user)
        except:
            user = self.context['owner']
            if user.is_authenticated:
                representation['is_favorite'] = self.is_favorite(instance, user)
        return representation

    @staticmethod
    def is_favorite(course, user):
        return user.favorites.filter(course=course).exists()


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'subject', 'preview', 'price']

    def to_representation(self, instance):
        representation = super(CourseListSerializer, self).to_representation(instance)
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        try:
            user = self.context['request'].user
            if user.is_authenticated:
                representation['is_favorite'] = self.is_favorite(instance, user)
        except:
            pass
        return representation

    @staticmethod
    def is_favorite(course, user):
        return user.favorites.filter(course=course).exists()

