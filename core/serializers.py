from  rest_framework import serializers
from .models import Pedido, Produto



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','preco','obs']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome']


class PedidoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id','date','produtos','obs','usuario','estabelecimento']

class PedidoMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id','date','produtos','obs','usuario','estabelecimento']