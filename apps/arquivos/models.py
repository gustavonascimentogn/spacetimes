from django.db import models
from django.contrib.auth.models import User
## from django_celery_results.models import TaskResult

class Arquivo(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, help_text='Instante de envio do arquivo')
    dataHoraInicioProcessamento = models.DateTimeField(default=None, null=True, blank=True, help_text='Instante de início de execução da Tarefa')
    dataHoraFimProcessamento = models.DateTimeField(default=None, null=True, blank=True, help_text='Instante de fim de execução da Tarefa')
    tempoExecucaoSegundos = models.FloatField(default=0, blank=True, null=True, verbose_name='Tempo de execução em segundos')
    nome = models.CharField(max_length=50, blank=False, verbose_name='Nome do documento')
    arquivo = models.FileField(upload_to='documentos',verbose_name='Anexe o documento')
    processado = models.BooleanField(default=False, verbose_name='Processado (marcado se Verdadeiro)')
    resultado_processamento = models.TextField(default=None, null=True, blank=True, verbose_name='Resultado do processamento')
    forma_envio = models.CharField(max_length=8, null=True, blank=True, verbose_name='Forma de envio')
    task_context = models.CharField(max_length=200, null=True, blank=True, verbose_name='Contexto da task')
    id_task = models.CharField(max_length=100, null=True, blank=True, verbose_name='ID Task')

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, verbose_name='User')


    class Meta:
        ordering = ["nome"]


    def __str__(self):
        return self.arquivo.name


    @property
    def tempoEsperaFila_segundos(self):
        if self.dataHoraInicioProcessamento and self.dataHoraCriacao:
            diferenca = self.dataHoraInicioProcessamento - self.dataHoraCriacao
            return diferenca.seconds
        else:
            return None


    @property
    def status_processamento(self):
        from celery.result import AsyncResult
        if self.id_task:
            res = AsyncResult(self.id_task)
            return res.state
        else:
            return 'NOT QUEUED'
