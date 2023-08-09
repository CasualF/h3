from rest_framework import serializers
from .models import Lesson, LessonContent
from question.serializers import QuestionSerializer


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'preview', 'created_at']


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(LessonDetailSerializer, self).to_representation(instance)
        representation['questions'] = QuestionSerializer(instance=instance.questions.all(), many=True).data
        representation['like_count'] = instance.likes.count()
        representation['contents'] = LessonContentSerializer(instance=instance.contents.all(), many=True).data

        user = self.context['request'].user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance, user)
            representation['is_disliked'] = self.is_disliked(instance, user)
        return representation

    @staticmethod
    def is_liked(lesson, user):
        return user.likes.filter(lesson=lesson).exists()

    @staticmethod
    def is_disliked(lesson, user):
        return user.dislikes.filter(lesson=lesson).exists()


class LessonContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonContent
        fields = ['name', 'file']
