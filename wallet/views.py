from django.shortcuts import render, redirect
from .models import Transacao, Categoria
from .forms import transacaoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def transacoes(request):
    data = {}
    data['transacao'] = Transacao.objects.all().filter(user=request.user)
    data['categoria'] = Categoria.objects.all().filter(user=request.user)
    return render(request, 'transacoes.html', data)


@login_required
def novaTransacao(request):
    data = {}
    form = transacaoForm(request.POST or None)
    if form.is_valid():
        transacao = form.save(commit= False)
        transacao.user = request.user 
        transacao.save()
        return redirect('historico-transacoes')
    data['form'] = form
    return render(request, 'nova-transacao.html', data)


@login_required
def updateTransacao(request, id):
    data = {}
    transacao = Transacao.objects.get(pk = id)
    form = transacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('historico-transacoes')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'nova-transacao.html', data)

@login_required
def delete(request, id):
    transacao = Transacao.objects.get(pk = id)
    transacao.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('historico-transacoes')
