from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Produto,Pedido
from .serializers import PedidoSerializer,ProdutoSerializer,PedidoMiniSerializer
# Create your views here.


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def list(self, request, *args, **kwargs):
        queryset = Pedido.objects.all()
        serializer = PedidoMiniSerializer(queryset, many=True)
        return Response(serializer.data)


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
