# Generated by Django 4.0.6 on 2022-08-06 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ez_rank', '0003_team_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added'),
        ),
    ]
