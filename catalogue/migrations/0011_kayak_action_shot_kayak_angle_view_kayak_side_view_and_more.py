# Generated by Django 4.0.6 on 2022-08-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_alter_kayak_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='kayak',
            name='action_shot',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kayak',
            name='angle_view',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kayak',
            name='side_view',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kayak',
            name='top_view',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
