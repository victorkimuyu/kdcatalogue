# Generated by Django 4.0.6 on 2022-08-25 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0020_remove_kayak_action_shot_remove_kayak_angle_view_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kayak',
            old_name='photo_path',
            new_name='photo',
        ),
    ]
