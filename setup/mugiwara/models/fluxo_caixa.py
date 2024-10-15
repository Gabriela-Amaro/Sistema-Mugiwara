from django.db import models

class fluxo_caixa(models.Model):
    data_inicial = models.DateField(auto_now_add=True)
    data_final = models.DateField(auto_now_add=True)
    saldo_inicial = models.DecimalField(decimal_places=2, max_digits=9)
    saldo_final = models.DecimalField(decimal_places=2, max_digits=9)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Período: {self.data_inicial} - {self.data_final}"