from django.db import models

from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pet(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    porte = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("CONFIRMADO", "Confirmado"),
        ("CANCELADO",  "Cancelado"),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    data = models.DateField()
    horario = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices = STATUS_CHOICES,
        default= "PENDENTE")

    def _str_(self):
        return f"{self.pet} - {self.data}"