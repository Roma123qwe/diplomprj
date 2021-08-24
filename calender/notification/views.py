import datetime
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event
from rest_framework import status
from .serializers import EventSerializer

class EventList(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = EventSerializer
    def get(self, request, **dates):
        notification_dict = {
            '': 'Нет',
            datetime.timedelta(seconds=3600): 'Да, за час',
            datetime.timedelta(seconds=7200): 'Да, за 2 часа',
            datetime.timedelta(seconds=14400): 'Да, за 4 часа',
            datetime.timedelta(seconds=86400): 'Да, за день',
            datetime.timedelta(seconds=604800): 'Да, за неделю',
        }
        self.queryset = Event.objects.filter(user_id=request.user.id)
        if 'date_from_input' in dates.keys():
            self.queryset = Event.objects.filter(user_id=request.user.id, date_from=dates['date_from_input'])
        if 'date_to_input' in dates.keys():
            self.queryset = Event.objects.filter(data_from_gte=datetime.datetime.strftime(dates['date_from_input'],'%Y-%m-%d'), \
                data_from__lte=(dates['date_to_input'], '%Y-%m-%d'), \
                user_id=request.user.id)
        serializer = self.get_serializer(self.queryset, many=True)
        for e in serializer.data:
            e['notificate'] = notification_dict[e['notificate']]
        return Response(serializer.data)

class EventCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        e = Event.objects.get(id=serializer.data['id'])
        if e.date_to == None:
            e.date_to = e.date_from.replace(hour=23, minute=59)
        e.notification_time = e.date_from - e.notificate
        e.save()
        serializer = self.get_serializer(e)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def notificate():
    evetns_for_notif = Event.objects.filter(notification_time__lte=datetime.datetime.today(), \
                                            was_notificate=False).select_related('user')
    for obj in evetns_for_notif:
        send_mail('Notification', obj.name + ' в '+ obj.date_from.strftime("%m-%d-%Y, %H:%M"), 'djangomyprj@gmail.com', obj.user.email )
        obj.was_notificate = True
        obj.save