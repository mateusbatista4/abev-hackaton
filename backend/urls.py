from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.views import ProdutoViewSet,PedidoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
