from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course


User = get_user_model()


class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Too bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excellent')
    )
    owner = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title
