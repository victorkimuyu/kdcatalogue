# Generated by Django 4.0.6 on 2022-08-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0019_remove_kayak_top_alter_kayak_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kayak',
            name='action_shot',
        ),
        migrations.RemoveField(
            model_name='kayak',
            name='angle_view',
        ),
        migrations.RemoveField(
            model_name='kayak',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='kayak',
            name='side_view',
        ),
        migrations.AddField(
            model_name='kayak',
            name='photo_path',
            field=models.URLField(blank=True, null=True, verbose_name='Photo URL'),
        ),
    ]
