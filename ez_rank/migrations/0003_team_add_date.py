# Generated by Django 4.0.6 on 2022-08-06 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ez_rank', '0002_team_k_factor_team_ranked_games_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 6, 21, 1, 5, 333207, tzinfo=utc), verbose_name='date added'),
        ),
    ]
