# Generated by Django 5.0.6 on 2024-05-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0016_delete_timer_remove_reservation_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='has_child',
            field=models.BooleanField(default=False),
        ),
    ]
