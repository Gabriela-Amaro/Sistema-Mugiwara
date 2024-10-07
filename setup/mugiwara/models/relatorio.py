from django.db import models

class relatorio(models.Model):
    class relatorio_tipo(models.IntegerChoices):
        RECEITA = 1, "Receita"
        DESPESA  = 2, "Despesa"

    tipo = models.IntegerField(
        choices =  relatorio_tipo
    )
    periodo_inicio = models.DateField(auto_now=False, auto_now_add=False)
    periodo_fim = models.DateField(auto_now=False, auto_now_add=False)
    arquivo_pdf  = models.FileField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Relatório de {self.periodo_inicio} à {self.periodo_fim}"