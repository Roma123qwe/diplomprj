from django.urls import path, include
from . import views

urlpatterns = [
    path('event_list/', views.EventList.as_view()),
    path('event_list/<str:date_from_input>/', views.EventList.as_view()),
    path('event_list/<str:date_from_input>/<str:date_to_input>/', views.EventList.as_view()),
    path('event_create/', views.EventCreate.as_view(), name='create-event'),
]