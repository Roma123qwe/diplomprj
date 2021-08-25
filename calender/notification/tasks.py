from celery import Celery, app
from celery import shared_task
from django.core.mail import send_mail
from .models import Event
import datetime

app = Celery('notification', broker='redis://localhost')


@shared_task(name='notificate')
def notificate():
    evetns_for_notif = Event.objects.filter(notification_time__lte=datetime.datetime.today(),
                                            was_notificate=False).select_related('user')
    for obj in evetns_for_notif:
        send_mail('Notification', obj.name + ' в '+ obj.date_from.strftime("%m-%d-%Y, %H:%M"), 'djangomyprj@gmail.com', obj.user.email )
        obj.was_notificate = True
        obj.save  