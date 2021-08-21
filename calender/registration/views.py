from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def register(request):
    if request.method == 'POST':
        User.objects.create_user(username=request.POST['username'],
                                 email=request.POST['username'],
                                 password=request.POST['password'])
        Token.objects.create(user=User.objects.get(username=request.POST['username']))
        return redirect('/login/')
    return render(request, 'account/register.html')

def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['Login'],
            password=request.POST['password']
            )
        if user is not None:
            login(request, user)
            return redirect("create-event")
    return render(request, 'account/login.html')


