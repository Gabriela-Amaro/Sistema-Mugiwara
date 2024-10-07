from django.db import models

class fluxo_caixa(models.Model):
    data = models.DateField(auto_now_add=True)
    saldo_inicial = models.DecimalField(decimal_places=2, max_digits=9)
    saldo_final = models.DecimalField(decimal_places=2, max_digits=9)
    projecao_entradas = models.DecimalField(decimal_places=2, max_digits=9)
    projecao_saidas = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.data