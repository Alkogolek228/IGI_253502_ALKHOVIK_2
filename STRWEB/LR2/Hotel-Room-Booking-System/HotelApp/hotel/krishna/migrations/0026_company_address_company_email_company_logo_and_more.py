# Generated by Django 5.1.1 on 2024-09-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0025_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
