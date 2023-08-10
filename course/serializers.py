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
        representation['duration'] = self.period_counter(instance)
        representation['lesson_count'] = instance.lessons.count()
        representation['lessons'] = LessonDetailSerializer(instance=instance.lessons.all(), many=True).data
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

    @staticmethod
    def period_counter(course):
        try:
            return (course.ends_at - course.starts_at) / 60 / 60 / 24
        except:
            return None


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'subject', 'preview', 'price']

    def to_representation(self, instance):
        representation = super(CourseListSerializer, self).to_representation(instance)
        representation['duration'] = self.period_counter(instance)
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        user = self.context['request'].user
        if user.is_authenticated:
            representation['is_favorite'] = self.is_favorite(instance, user)
        return representation

    @staticmethod
    def is_favorite(course, user):
        return user.favorites.filter(course=course).exists()

    @staticmethod
    def period_counter(course):
        try:
            return (course.ends_at - course.starts_at) / 60 / 60 / 24
        except:
            return None
