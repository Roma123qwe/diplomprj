from django.urls import path, include

from . import views

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.login_user, name='login')
]
