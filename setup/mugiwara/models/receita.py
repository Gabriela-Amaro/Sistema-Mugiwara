from django.db import models

class categoria_choices_receita(models.IntegerChoices):
    C1 = 1, "Categoria 1"
    C2 = 2, "Categoria 2"
    C3 = 3, "Categoria 3"
    C4 = 4, "Categoria 4"

class receita(models.Model):
    class status_choices(models.IntegerChoices):
        ABERTO = 1, "Em Aberto"
        PAGO = 2, "Pago"


    descricao = models.TextField()
    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    categoria = models.IntegerField(
        choices = categoria_choices_receita,
        default = categoria_choices_receita.C1
    )
    status = models.IntegerField(
        choices = status_choices,
        default = status_choices.ABERTO
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"vencimento: {self.data_vencimento}, valor: {self.valor}"
