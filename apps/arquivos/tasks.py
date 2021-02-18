from celery.utils.log import get_task_logger
from pandas import DataFrame
from unipath import Path
from datetime import datetime
import time
import timeit
from django_celery_results.models import TaskResult

from celery import shared_task
from django.http import JsonResponse

from apps.arquivos.models import Arquivo

@shared_task(bind=True)
def processar_arquivo(self, pk_arquivo):
    time.sleep(5) ## Em processamento local, com arquivos de tamanho reduzido, a tarefa iniciava sua execução
                    ## antes de o arquivo ser salvo. Por isso este sleep de 5 segundos.

    ### início do processamento do arquivo
    inicio = timeit.default_timer() ## Usando timeit
    inicio_datetime = datetime.now()
    arquivo = Arquivo.objects.get(pk=pk_arquivo)
    arquivo.dataHoraInicioProcessamento = inicio_datetime

    COLUNAS = ['letra_inicial','palavras']
    if arquivo.arquivo.name.find('.csv') != -1 or arquivo.arquivo.name.find('.txt') != -1:
        dados = open(arquivo.arquivo.path)
        lista_palavras = dados.read().upper().split()
        df = DataFrame(columns=COLUNAS)
        for palavra in lista_palavras:
            nova_linha = {'letra_inicial':palavra[0],'palavras':palavra}
            df = df.append(nova_linha, ignore_index=True)

        df_results = df.groupby('letra_inicial').palavras.count()
        arquivo.resultado_processamento = df_results.to_json(orient='index')
    else:
        arquivo.resultado_processamento = 'Arquivo não possui extensão .csv ou .txt'

    arquivo.processado = True
    arquivo.dataHoraFimProcessamento = datetime.now()
    ### fim do processamento do arquivo
    fim = timeit.default_timer()
    arquivo.tempoExecucaoSegundos = fim - inicio
    arquivo.task_context = format(self.request)
    arquivo.save()
    return True

