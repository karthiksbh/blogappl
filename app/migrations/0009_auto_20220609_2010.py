# Generated by Django 3.2.8 on 2022-06-09 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(max_length=255),
        ),
    ]
