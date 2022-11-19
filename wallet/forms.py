from django.forms import ModelForm
from .models import Transacao, Categoria
from django import forms
import datetime

class transacaoForm(ModelForm):
    
    class Meta:
        model = Transacao
        fields = ['data', 'valor', 'descricao', 'categoria', 'observacao']




