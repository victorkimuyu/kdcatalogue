# Generated by Django 4.0.6 on 2022-08-14 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_kayak_action_shot_kayak_angle_view_kayak_side_view_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kayak',
            old_name='top_view',
            new_name='photo',
        ),
    ]
