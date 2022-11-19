from django.urls import path
from blog.views import landingPage, plataforma, sobrenos

urlpatterns = [
    path('', landingPage, name='landing-page'),
    path('plataforma/', plataforma, name='url_plataforma'),
    path('sobre-nos/', sobrenos, name='url_sobrenos')
]
