from rest_framework import serializers
from .models import Question, Answer
from lesson.models import Lesson


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(QuestionSerializer, self).to_representation(instance)
        representation['right_answer'] = self.get_right_answer(
            Question.objects.get(lesson=instance.lesson)
        )
        representation['wrong_answers'] = ",".join([i.answer for i in instance.answers.all() if not i.correct])
        try:
            user = self.context['request'].user
            if user.is_authenticated:
                representation['is_answered'] = self.is_answered(instance, user)
        except:
            try:
                user = self.context['owner']
                if user.is_authenticated:
                    representation['is_answered'] = self.is_answered(instance, user)
            except:
                pass
        return representation

    @staticmethod
    def get_right_answer(question):
        answer = "".join([i.answer for i in question.answers.all() if i.correct])
        return answer

    @staticmethod
    def is_answered(question, user):
        return user.correct_answers.filter(answer__question=question).exists()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
