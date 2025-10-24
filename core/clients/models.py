from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=150)  # nome do contato principal ou responsável
    cnpj = models.CharField(max_length=18, unique=True)  # formato 00.000.000/0000-00
    razao_social = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_fantasia or self.razao_social}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["razao_social"]
