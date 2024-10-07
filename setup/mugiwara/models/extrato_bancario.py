from django.db import models
from .conta_bancaria import conta_bancaria
        
class extrato_bancario(models.Model):
    arquivo_extrato = models.FileField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)
    conta_bancaria_id = models.ForeignKey(
        conta_bancaria,
        on_delete = models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"data: {self.created_at}, conta: {self.conta_bancaria.numero_conta}"
