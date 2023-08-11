# Generated by Django 4.2.4 on 2023-08-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_total_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9),
        ),
    ]
