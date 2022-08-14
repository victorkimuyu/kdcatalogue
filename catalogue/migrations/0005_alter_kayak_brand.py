# Generated by Django 4.0.6 on 2022-08-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_alter_kayak_model_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayak',
            name='brand',
            field=models.CharField(blank=True, choices=[('AZ', 'Azul Kayaks'), ('CB', 'Cobra Kayaks'), ('RT', 'Riot Kayaks'), ('Rs', 'Riot SUP Kayaks'), ('BR', 'Boreal Design')], max_length=20, null=True, verbose_name='Brand'),
        ),
    ]