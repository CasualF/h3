from django.db import models
from course.models import Course


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='images/lesson_previews/', null=True, blank=True)
    youtube_link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course.title} -> {self.title}'


class LessonContent(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, related_name='contents', on_delete=models.CASCADE)
    file = models.FileField(upload_to=f'media/lesson_content/')
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_name(self):
        from random import randint
        return 'content' + str(self.id) + str(randint(1000, 10000))

    def save(self, *args, **kwargs):
        self.name = self.generate_name()
        return super(LessonContent, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.lesson.title} -> {self.name}'
