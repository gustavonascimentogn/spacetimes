from django.db import models

from django.contrib.auth.models import User

class Arquivo(models.Model):
    nome = models.CharField(max_length=50, blank=False, verbose_name='Nome do documento')
    arquivo = models.FileField(upload_to='documentos',verbose_name='Anexe o documento')

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, verbose_name='User')

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
