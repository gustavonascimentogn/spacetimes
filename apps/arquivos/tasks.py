from pandas import DataFrame
from unipath import Path
from datetime import datetime
import time
import timeit

from celery import shared_task
from django.http import JsonResponse

from apps.arquivos.models import Arquivo


def contar_palavras():
    print('qualquer coisa')


@shared_task
def processar_arquivo(pk_arquivo):
    time.sleep(10) ## para forçar a tarefa a ter um tempo mais longo de duração
    arquivo = Arquivo.objects.filter(pk=pk_arquivo)

    ### início do processamento do arquivo
    COLUNAS = ['letra_inicial','palavras']

    ### início processamento do arquivo ###
    arquivo.dataHoraInicioProcessamento = datetime.now()
    inicio = timeit.default_timer()

    if arquivo.arquivo.name.find('.csv') != -1 or arquivo.arquivo.name.find('.txt') != -1:
        dados = open(arquivo.arquivo.path)
        lista_palavras = dados.read().split()
        df = DataFrame(columns=COLUNAS)
        for palavra in lista_palavras:
            nova_linha = {'letra_inicial':palavra[0],'palavras':palavra}
            df = df.append(nova_linha, ignore_index=True)

        df_results = df.groupby('letra_inicial').palavras.count()
        arquivo.resultado_processamento = df_results.to_json(orient='index')
    else:
        arquivo.resultado_processamento = 'Arquivo não possui extensão .csv ou .txt'

    arquivo.processado = True
    ### fim do processamento do arquivo

    arquivo.dataHoraFimProcessamento = datetime.now()
    fim = timeit.default_timer()
    arquivo.tempoExecucaoSegundos = fim - inicio
    ### fim processamento do arquivo
    arquivo.save()
    return True

