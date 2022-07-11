# Generated by Django 4.0.6 on 2022-07-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayak',
            name='model_name',
            field=models.CharField(choices=[('AZ', 'Axul Kayaks'), ('CB', 'Cobra Kayaks'), ('RT', 'Riot Kayaks'), ('BR', 'Boreal Design')], max_length=50, primary_key=True, serialize=False, verbose_name='Model'),
        ),
    ]