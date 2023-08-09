from django.db import models
from lesson.models import Lesson
from django.contrib.auth import get_user_model

User = get_user_model()


class QuestionStatus(models.TextChoices):
    in_process = 'in_process'
    completed = 'completed'


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE, unique=True)
    body = models.TextField()
    # status = models.CharField(max_length=30, choices=QuestionStatus.choices, default=QuestionStatus.in_process)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.lesson.title} -> {self.body}'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, blank=True, null=True)
    correct = models.BooleanField()

    def __str__(self):
        return f'{self.question.body} -> {self.answer}'

    class Meta:
        unique_together = ['question', 'answer']


class CorrectAnswer(models.Model):
    owner = models.ForeignKey(User, related_name='correct_answers', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner.email} -> {self.answer}'
