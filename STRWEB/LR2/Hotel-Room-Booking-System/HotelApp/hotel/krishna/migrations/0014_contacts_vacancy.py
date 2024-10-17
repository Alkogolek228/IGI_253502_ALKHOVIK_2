# Generated by Django 5.0.6 on 2024-05-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0013_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='This is a contact')),
                ('phonenumber', models.CharField(max_length=15)),
                ('email', models.EmailField(default='defalt@gmail.com', max_length=254)),
                ('img', models.ImageField(blank=True, upload_to='contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Vacancy', max_length=200)),
                ('text', models.TextField(default='We are hiring!')),
            ],
        ),
    ]
