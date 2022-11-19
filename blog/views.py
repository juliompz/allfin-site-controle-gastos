from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def landingPage(request):
    return render(request, 'landing.html')

@login_required
def plataforma(request):
    return render(request, 'plataforma.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')
