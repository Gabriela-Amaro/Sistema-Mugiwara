from django.db import models

class conta_bancaria(models.Model):
    nome_banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=3)
    numero_conta = models.CharField(max_length=50)
    saldo_atual = models.DecimalField(decimal_places=2, max_digits=9, default=0, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        ordering = ['id', '-created_at', 'nome_banco']

    def __str__(self):
        return f"id: {self.id}, Banco: {self.nome_banco}, agencia: {self.agencia}, conta: {self.numero_conta}, saldo: {self.saldo_atual}"
