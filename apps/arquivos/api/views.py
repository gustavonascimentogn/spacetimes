from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


# ViewSets define the view behavior.
from apps.arquivos.api.serializers import ArquivoSerializer
from apps.arquivos.models import Arquivo


class ArquivoViewSet(viewsets.ModelViewSet):

        queryset = Arquivo.objects.all()
        serializer_class = ArquivoSerializer
        parser_classes = (MultiPartParser, FormParser,)

        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        http_method_names = ['post']

        ######################


        def get_queryset(self, *args, **kwargs):
            qs = super(ArquivoViewSet, self).get_queryset(*args, **kwargs)
            qs = qs.filter(user=self.request.user)
            return qs

        '''
        ## Bloqueando acesso a esta operação
        def update(self, request, pk=None):
            response = {'message': 'Update function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


        ## Bloqueando acesso a esta operação
        def partial_update(self, request, pk=None):
            response = {'message': 'Update function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


        ## Bloqueando acesso a esta operação
        def destroy(self, request, pk=None):
            response = {'message': 'Delete function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        '''

