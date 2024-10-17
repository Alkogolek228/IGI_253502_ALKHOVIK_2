# Generated by Django 5.0.6 on 2024-05-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0007_promocode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
