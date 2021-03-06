# Generated by Django 3.2.6 on 2021-08-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_alter_event_notificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='notificaton_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='was_notificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='notificate',
            field=models.IntegerField(choices=[[1, 'За неделю'], [2, 'За день'], [3, 'За 4 часа'], [4, 'За 2 часа'], [5, 'За час']], default=3),
        ),
    ]
