from rest_framework import serializers
from .models import Lesson, LessonContent


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'preview', 'created_at']


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(LessonDetailSerializer, self).to_representation(instance)
        representation['contents'] = LessonContentSerializer(instance=instance.contents.all(), many=True)
        return representation


class LessonContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonContent
        fields = ['name', 'file']
