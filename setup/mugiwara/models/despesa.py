from django.db import models
from .fornecedor import fornecedor

class despesa(models.Model):
    class status_choices(models.IntegerChoices):
        ABERTO = 1, "Em Aberto"
        PAGO = 2, "Pago"

    descricao = models.TextField()
    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    categoria = models.CharField(max_length=50)
    status = models.IntegerField(
        choices = status_choices,
        default = status_choices.ABERTO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    fornecedor_id = models.ForeignKey(
        fornecedor,
        on_delete = models.SET_NULL,
        null = True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"vencimento: {self.data_vencimento}, valor: {self.valor}"