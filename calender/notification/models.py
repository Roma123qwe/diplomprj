from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
grade_list = (
    [timedelta(days=7), 'За неделю'],
    [timedelta(days=1), 'За день'],
    [timedelta(hours=4), 'За 4 часа'],
    [timedelta(hours=2), 'За 2 часа'],
    [timedelta(hours=1), 'За час'],
)
class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Events')
    name = models.CharField(max_length=50)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(blank=True, null=True)
    notificate = models.DurationField(choices=grade_list, default=3, null=True, blank=True)
    notification_time = models.DateTimeField(null=True, blank=True)
    was_notificate = models.BooleanField(default=False)