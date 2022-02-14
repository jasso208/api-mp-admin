from django.db import models
from django.contrib.auth.models import User
from .Proveedor import Proveedor

class Articulo(models.Model):
    nombre = models.CharField(max_length = 100,null = False,blank = False,default = '')
    descripcion = models.CharField(max_length = 500, null=False, blank=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT,related_name='proveedor_articulo')
    precio_compra_sin_iva = models.DecimalField(max_digits = 30, decimal_places = 2,default = 0.00)
    iva = models.DecimalField(max_digits = 30,decimal_places = 2,default = 0.00)
    precio_compra_con_iva =  models.DecimalField(max_digits = 20,decimal_places = 2,default = 0.00)
    usuario_alta = models.ForeignKey(User, on_delete=models.PROTECT,related_name = "usuario_alta")
    fecha_alta = models.DateTimeField(auto_now_add=True)
    usuario_modifica = models.ForeignKey(User, on_delete=models.PROTECT,related_name ="usuario_modifica")
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    activo = models.CharField(max_length = 1,default="S",choices = [('S','S'),('N','N')])
    
    def __str__(self):
        return self.nombre