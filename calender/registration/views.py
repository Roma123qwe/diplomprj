from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from calender.registration.models import MyUser


def register(request):
    if request.method == 'POST':
        if 'email' in request.POST.keys():
            MyUser.objects.create_user(username=request.POST['username'],
                                 email=request.POST['email'],
                                 password=request.POST['password'])
            Token.objects.create(user=MyUser.objects.get(username=request.POST['email']))
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': 'Email not valid'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            email=request.POST['email'],
            password=request.POST['password']
            )
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


