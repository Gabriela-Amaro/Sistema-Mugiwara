from django.db import models

class conta_bancaria(models.Model):
    nome_banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=3)
    numero_conta = models.CharField(max_length=50)
    saldo_atual = models.DecimalField(decimal_places=2, max_digits=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome_banco', 'saldo_atual']

    def __str__(self):
        return f"Banco: {self.nome_banco}, agencia: {self.agencia}, conta: {self.numero_conta}"
