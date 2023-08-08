from django.db import models
from django.utils.text import slugify


class Subject(models.Model):
    slug = models.SlugField(max_length=200, unique=True, primary_key=True, blank=True)
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='images/course_previews/', blank=True, null=True, default=None)
    price = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
