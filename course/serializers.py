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
        return representation


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'preview', 'price']

    def to_representation(self, instance):
        representation = super(CourseListSerializer, self).to_representation(instance)
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        return representation
