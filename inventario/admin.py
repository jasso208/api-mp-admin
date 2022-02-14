from django.contrib import admin
from inventario.models.Articulo import Articulo
from inventario.models.Color import Color
from inventario.models.VariacionArticulo import VariacionArticulo
from inventario.models.Proveedor import Proveedor
# Register your models here.

admin.site.register(Articulo)
admin.site.register(Color)
admin.site.register(VariacionArticulo)
admin.site.register(Proveedor)