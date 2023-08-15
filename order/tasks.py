from django.core.mail import send_mail
from config.celery import app


@app.task(bind=True)
def send_order_notification(self, user_email, order_id):
    activation_url = f'http://localhost:3000/api/orders/confirm/{order_id}/'
    subject = 'Hello, confirm your order:'

    send_mail(
        subject,
        f'Click the link to confirm your order\n{activation_url}',
        'dastan12151@gmail.com',
        [user_email],
        fail_silently=True
    )
