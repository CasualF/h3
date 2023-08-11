from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import send_order_notification

User = get_user_model()


class OrderStatus(models.TextChoices):
    in_process = 'in_process'
    completed = 'completed'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.course.title


class Order(models.Model):
    owner = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    course = models.ManyToManyField(Course, through=OrderItem)
    status = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.in_process)
    total_sum = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f'{self.id} -> {self.course}'


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, *args, **kwargs):
    if created:
        send_order_notification(instance.owner.email, instance.id)

