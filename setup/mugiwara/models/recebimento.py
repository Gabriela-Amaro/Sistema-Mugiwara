from django.db import models
from .receita import receita

class recebimento(models.Model):
    class  metodos_recebimento(models.IntegerChoices):
        DINHEIRO = 1, "Dinheiro"
        PIX = 2, "Pix"

    valor_pago = models.DecimalField(decimal_places=2, max_digits=9)
    metodo_recebimento = models.IntegerField(
        choices = metodos_recebimento,
        default = metodos_recebimento.DINHEIRO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    receita_id = models.ForeignKey(
        receita,
        on_delete = models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"data: {self.created_at}, valor: {self.valor_pago}"
