# Generated by Django 5.0.6 on 2024-05-11 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0015_timer_reservation_created_at_reservation_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Timer',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='updated_at',
        ),
    ]
