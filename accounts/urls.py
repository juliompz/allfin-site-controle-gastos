from django.urls import path
from .views import logar, register, sair

urlpatterns = [
   path('register/', register, name='register-form'),
   path('login/', logar, name='login-form'),
   path('deslogar', sair, name='sair'),
]
