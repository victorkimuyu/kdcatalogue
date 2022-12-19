# Generated by Django 4.0.6 on 2022-12-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_alter_kayak_brand_alter_kayak_model_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayak',
            name='beluga_skirt_size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Beluga Skirt'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='height',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='ideal_paddler_size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Paddler Size'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='length',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='paddling',
            field=models.CharField(blank=True, choices=[('Solo', 'Solo'), ('Tandem', 'Tandem')], max_length=50, null=True, verbose_name='Paddling'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='steering',
            field=models.CharField(blank=True, choices=[('Rudder', 'Rudder'), ('Skeg', 'Skeg'), ('Both', 'Both')], max_length=50, null=True, verbose_name='Steering'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='width',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Width'),
        ),
    ]
