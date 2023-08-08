from rest_framework import serializers
from django.db.models import Avg
from .models import Course, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(CourseSerializer, self).to_representation(instance)
        representation['rating'] = instance.reviews.aggregate(Avg('rating'))
        return representation
