from rest_framework import generics, permissions, mixins
from .models import Question, Answer, CorrectAnswer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response


class QuestionView(generics.RetrieveAPIView, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return permissions.IsAuthenticated(),
        return permissions.IsAdminUser(),

    def post(self, request, pk, *args, **kwargs):
        question = self.get_object()
        user = request.user
        data = request.data
        answer = data.get('answer')
        for i in question.answers.all():
            if answer == i.answer and i.correct:
                if not user.correct_answers.filter(answer=i).exists:
                    correct_answer = CorrectAnswer.objects.create(owner=user, answer=i)
                    correct_answer.save()
                return Response('Correct answer')
        return Response('Wrong answer')
