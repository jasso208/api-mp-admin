from turtle import color
from django.db import models
from .Articulo import Articulo
from .Color import Color

class VariacionArticulo(models.Model):
    articulo = models.ForeignKey(Articulo,on_delete = models.PROTECT,related_name="variacion_list")
    color = models.ForeignKey(Color, on_delete = models.PROTECT,related_name="variacion_color")
    
    class Meta:
        unique_together = ("articulo","color")
    
    
    