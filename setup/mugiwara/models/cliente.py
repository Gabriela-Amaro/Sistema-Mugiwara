from django.db import models

class cliente(models.Model):
    nome = models.CharField(max_length=100)
    cnpj_cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email =  models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome