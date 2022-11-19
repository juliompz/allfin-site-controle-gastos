from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "GET":
         return render(request,'registration/register.html')
    else:
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        email = request.POST.get('email', None)
        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse('Ja existe um usuario com esse nome')
    user = User.objects.create_user(username=usuario, email=email, password=senha)
    user.save()
    return redirect('login-form')

def logar(request):
    if request.method == "GET":
        return render(request, 'registration/login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('url_plataforma')
        else:
            return HttpResponse('Usuario ou senha invalidos')

def sair(request):
    logout(request)
    return redirect('/')


   