# Generated by Django 5.0.6 on 2025-04-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractuser',
            name='is_worker_active',
            field=models.BooleanField(default=True),
        ),
    ]
