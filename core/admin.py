from django.contrib import admin
from .models import Produto,Pedido,Usuario,Bar
# Register your models here.
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Bar)