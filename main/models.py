from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Usuario(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self) -> str:
      return self.user.username
class Balanco(models.Model):
  user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  date = models.DateField(default=timezone.now)
  def __str__(self):
      return "Balanço do mês de: "+ str(self.mes()) +" do usuário "+ str(self.user)
  def mes(self):
    mes = self.date.month
    if mes == 1:
      return "janeiro"
    if mes == 2:
      return "fevereiro"
    if mes == 3:
      return "março"
    if mes == 4:
      return "abril"
    if mes == 5:
      return "maio"
    if mes == 6:
      return "junho"
    if mes == 7:
      return "julho"
    if mes == 8:
      return "agosto"
    if mes == 9:
      return "setembro"
    if mes == 10:
      return "outubro"
    if mes == 11:
      return "novembro"
    if mes == 12:
      return "dezembro"
  def receita_total(self):
    receita = 0
    for recei in self.receita_set.all():
      receita+= recei.valor
    return receita
  def despesa_total(self):
    despesa = 0
    for desp in self.despesa_set.all():
      despesa+=desp.valor
    return despesa
    
  def saldo(self):
    num = self.receita_total() - self.despesa_total()
    return "{:.2f}".format(num)

class Receita(models.Model):
  descricao = models.CharField(max_length=100)
  valor = models.FloatField(default=0.0)
  date = models.DateField(default=timezone.now)
  balanco = models.ForeignKey(Balanco, on_delete=models.CASCADE)
  def __str__(self) -> str:
      return self.descricao + " " + str(self.date)
class Despesa(models.Model):
  descricao = models.CharField(max_length=100)
  valor = models.FloatField(default=0.0)
  date = models.DateField(default=timezone.now)
  balanco = models.ForeignKey(Balanco, on_delete=models.CASCADE)
  def __str__(self) -> str:
      return self.descricao + " " + str(self.date)
