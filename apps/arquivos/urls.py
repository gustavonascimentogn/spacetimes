from django.urls import path
from .views import ArquivoNovo, ArquivoEdit, ArquivoDelete, ArquivosList

urlpatterns = [
    path('<str:mensagem>', ArquivosList.as_view(), name='list_arquivos'),
    path('', ArquivosList.as_view(), name='list_arquivos'),
    path('novo/', ArquivoNovo.as_view(), name='create_arquivo'),
    path('delete/<int:pk>', ArquivoDelete.as_view(), name='delete_arquivo'),
    path('editar/<int:pk>', ArquivoEdit.as_view(), name='update_arquivo'),
]
