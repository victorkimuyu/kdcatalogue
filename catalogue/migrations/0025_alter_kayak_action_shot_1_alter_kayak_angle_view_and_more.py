# Generated by Django 4.0.6 on 2022-08-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0024_alter_kayak_action_shot_1_alter_kayak_action_shot_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayak',
            name='action_shot_1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Action Shot 1'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='angle_view',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Angle View'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='side_view',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Side View'),
        ),
        migrations.AlterField(
            model_name='kayak',
            name='top_view',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Top View'),
        ),
    ]