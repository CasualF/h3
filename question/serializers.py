from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(QuestionSerializer, self).to_representation(instance)
        representation['answers'] = AnswerSerializer(instance=instance.answers.all(), many=True).data
        try:
            user = self.context['request'].user
        except:
            user = self.context['owner']
        if user.is_authenticated:
            representation['is_answered'] = self.is_answered(instance, user)
        return representation

    @staticmethod
    def is_answered(question, user):
        return user.correct_answers.filter(answer__question=question).exists()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
