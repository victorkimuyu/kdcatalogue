# Generated by Django 4.0.6 on 2022-08-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_rename_top_view_kayak_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayak',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
