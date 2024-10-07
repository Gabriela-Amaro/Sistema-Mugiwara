from django.db import models

class usuario(models.Model):
    class role_opt(models.IntegerChoices):
        ADMIN = 1, "Administrador"
        USUARIO = 2, "Usuário"

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha_hash = models.CharField(max_length=254)
    role = models.IntegerField(
        choices = role_opt,
        default = role_opt.USUARIO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome