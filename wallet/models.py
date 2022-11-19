from django.db import models
from django.contrib.auth import get_user_model

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    descricao = models.CharField(max_length = 100, verbose_name='Descrição')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits = 7, decimal_places = 2)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    observacao = models.TextField(null = True, blank = True)

    def getValor(self):
        return self.valor

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Transações'



    

