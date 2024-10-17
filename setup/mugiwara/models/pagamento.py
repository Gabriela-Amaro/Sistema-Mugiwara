from django.db import models
from .despesa import despesa
from .conta_bancaria import conta_bancaria

class pagamento(models.Model):
    class  metodos_pagamento(models.IntegerChoices):
        DINHEIRO = 1, "Dinheiro"
        DEBITO  = 2, "Débito em conta"

    valor_pago = models.DecimalField(decimal_places=2, max_digits=9, auto_created=True)
    metodo_pagamento = models.IntegerField(
        choices = metodos_pagamento,
        default = metodos_pagamento.DINHEIRO,
    )
    created_at  =  models.DateTimeField(auto_now_add=True, auto_created=True)
    despesa_id = models.ForeignKey(
        despesa,
        on_delete =  models.CASCADE
    )
    conta_bancaria_id  = models.ForeignKey(
        conta_bancaria,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"data: {self.created_at}, valor: {self.valor_pago}"