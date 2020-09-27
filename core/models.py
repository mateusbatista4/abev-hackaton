from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    adress = models.CharField(max_length=150)

    def __str__(self):
        return self.name + " " + self.surname

class Bar(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    adress = models.CharField(max_length=150)
    def __str__(self):
        return self.name


class Produto(models.Model):
    nome = models.CharField(max_length=70)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    obs = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.nome



class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto,blank=True,null=True)
    obs = models.CharField(max_length=250)
    date = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True,blank=True,related_name="usuario")  #possibilidade de mais de um (ManyToManyField)
    estabelecimento = models.ForeignKey(Bar, on_delete=models.CASCADE,null=True,blank=True,related_name="estabeleciento")

    def __str__(self):
        return "Pedido "+ str(self.id)