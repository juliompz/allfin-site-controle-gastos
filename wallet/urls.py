from django.urls import path, include
from .views import transacoes, novaTransacao, updateTransacao, delete

urlpatterns = [
    path('transacoes/', transacoes, name='historico-transacoes'),
    path('nova-transacao/', novaTransacao, name='url_nova-transacao'),
    path('updateTransacao/<int:id>/',updateTransacao, name= 'url_update'),
    path('delete/<int:id>/',delete, name= 'url_delete'),
]