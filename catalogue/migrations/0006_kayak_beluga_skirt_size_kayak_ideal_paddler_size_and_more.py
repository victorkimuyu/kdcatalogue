# Generated by Django 4.0.6 on 2022-07-12 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_remove_kayak_discontinued_alter_kayak_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='kayak',
            name='beluga_skirt_size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='kayak',
            name='ideal_paddler_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kayak',
            name='outer_cockpit_dimensions',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
