# Generated by Django 3.2.6 on 2021-08-19 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_alter_event_notificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notificate',
            field=models.DurationField(choices=[[datetime.timedelta(days=7), 'За неделю'], [datetime.timedelta(days=1), 'За день'], [datetime.timedelta(seconds=14400), 'За 4 часа'], [datetime.timedelta(seconds=7200), 'За 2 часа'], [datetime.timedelta(seconds=3600), 'За час']], default=3),
        ),
    ]
