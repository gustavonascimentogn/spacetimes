from rest_framework import serializers

# API REST
# Serializers define the API representation.
from apps.arquivos.models import Arquivo
from ..tasks import processar_arquivo

class ArquivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arquivo
        fields = ['nome','arquivo']


    def create(self, validated_data):
        arquivo = Arquivo(
            nome=validated_data['nome'],
            arquivo=validated_data['arquivo']
        )
        arquivo.user = self.context['request'].user
        arquivo.forma_envio = 'API'
        arquivo.save()
        processar_arquivo.delay(arquivo.pk)
        return(arquivo)

