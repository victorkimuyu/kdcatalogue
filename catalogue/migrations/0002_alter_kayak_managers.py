# Generated by Django 4.0.6 on 2022-08-08 05:43

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='kayak',
            managers=[
                ('kayaks', django.db.models.manager.Manager()),
            ],
        ),
    ]
