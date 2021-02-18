import json
from datetime import datetime

from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token, ensure_csrf_cookie
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Arquivo
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import processar_arquivo
from django_celery_results.models import TaskResult


## Class para processamento requisição ajax
class AtualizaStatusTask(LoginRequiredMixin,View):

    def post(self, request, *args, **kwargs):
        id_task = self.kwargs['id_task']
        from celery.result import AsyncResult
        res = AsyncResult(id_task)
        response = json.dumps({'status':res.state})
        return HttpResponse(response, content_type='application/json')


class ArquivosList(LoginRequiredMixin,ListView):
    model = Arquivo
    paginate_by = 20

    ## Listando somente arquivos do user logado
    def get_queryset(self):
        user_logado = self.request.user
        return Arquivo.objects.filter(user=user_logado).order_by('-pk')


class ArquivoEdit(LoginRequiredMixin,UpdateView):
    model = Arquivo
    fields = ['nome','arquivo']

    def form_valid(self, form):
        arquivo = form.save(commit=False)
        user_logado = self.request.user
        arquivo.resultado_processamento = None
        arquivo.tempoExecucaoSegundos = None
        arquivo.dataHoraCriacao = datetime.now()
        arquivo.dataHoraInicioProcessamento = None
        arquivo.dataHoraFimProcessamento = None
        arquivo.processado = False
        arquivo.user = user_logado
        arquivo.forma_envio='Browser'
        x = processar_arquivo.delay(arquivo.pk)
        arquivo.id_task = x.task_id
        arquivo.save()

        from django.shortcuts import redirect
        return redirect('list_arquivos', 'Tarefa incluída na fila para execução.')

class ArquivoDelete(LoginRequiredMixin,DeleteView):
    model = Arquivo
    success_url = reverse_lazy('list_arquivos')


class ArquivoNovo(LoginRequiredMixin,CreateView):
    model = Arquivo
    fields = ['nome','arquivo']

    def form_valid(self, form):
        arquivo = form.save(commit=False)
        user_logado = self.request.user
        arquivo.user = user_logado
        arquivo.forma_envio = 'Browser'
        arquivo.save() ## save para gerar a PK
        x = processar_arquivo.delay(arquivo.pk)
        arquivo.id_task = x.task_id
        arquivo.save() ## save para salvar a id_task


        from django.shortcuts import redirect
        return redirect('list_arquivos','Tarefa incluída na fila para execução.')






