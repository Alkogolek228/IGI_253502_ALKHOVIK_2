# Generated by Django 5.1.1 on 2024-09-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0020_news_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('definition', models.TextField()),
            ],
        ),
    ]
