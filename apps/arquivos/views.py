from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Arquivo
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import processar_arquivo


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
        arquivo.user = user_logado
        arquivo.forma_envio='Browser'
        arquivo.save()
        processar_arquivo.delay(arquivo.pk)

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
        arquivo.save()
        processar_arquivo.delay(arquivo.pk)

        from django.shortcuts import redirect
        return redirect('list_arquivos','Tarefa incluída na fila para execução.')






