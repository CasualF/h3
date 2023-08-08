from rest_framework import serializers
from django.db.models import Avg
from .models import Course, Subject


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
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        representation['favorite_count'] = instance.favorites.count()
        user = self.context['request'].user
        if user.is_authenticated:
            representation['is_favorite'] = self.is_favorite(instance, user)
        return representation

    @staticmethod
    def is_favorite(video, user):
        return user.favorites.filter(video=video).exists()


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'preview', 'price']

    def to_representation(self, instance):
        representation = super(CourseListSerializer, self).to_representation(instance)
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        # representation['favorite_count'] = instance.favorites.count()
        user = self.context['request'].user
        if user.is_authenticated:
            representation['is_favorite'] = self.is_favorite(instance, user)
        return representation

    @staticmethod
    def is_favorite(video, user):
        return user.favorites.filter(video=video).exists()