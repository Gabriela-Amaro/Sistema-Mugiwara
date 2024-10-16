from django.db import models

class fluxo_caixa(models.Model):
    data_inicial = models.DateField()
    data_final = models.DateField()
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Período: {self.data_inicial} - {self.data_final}"