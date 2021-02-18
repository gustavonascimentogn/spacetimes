from django.urls import path
from .views import ArquivoNovo, ArquivoEdit, ArquivoDelete, ArquivosList, AtualizaStatusTask

urlpatterns = [
    path('<str:mensagem>', ArquivosList.as_view(), name='list_arquivos'),
    path('', ArquivosList.as_view(), name='list_arquivos'),
    path('novo/', ArquivoNovo.as_view(), name='create_arquivo'),
    path('delete/<int:pk>', ArquivoDelete.as_view(), name='delete_arquivo'),
    path('editar/<int:pk>', ArquivoEdit.as_view(), name='update_arquivo'),
    path('get_task_status/<str:id_task>', AtualizaStatusTask.as_view(), name='get_task_status'),
]
