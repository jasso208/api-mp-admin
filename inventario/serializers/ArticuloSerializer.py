from inventario.models.VariacionArticulo import VariacionArticulo
from rest_framework import serializers
from ..models.Articulo import Articulo
from ..serializers.ProveedorSerializer import ProveedorSerializer
from ..serializers.UserSerializer import UserSerializer
from ..serializers.VariacionArticuloSerializer import VariacionArticuloSerializer
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

class ArticuloSerializer(serializers.ModelSerializer):
    proveedor_det = ProveedorSerializer(read_only=True,source="proveedor")
    usuario_alta_det = UserSerializer(read_only=True,source = "usuario_alta")
    usuario_modifica_det = UserSerializer(read_only = True,source = "usuario_modifica")
    variacion_list = VariacionArticuloSerializer(read_only=True,many = True)
    
    class Meta:
        model = Articulo
        fields = ("id","nombre","descripcion","precio_compra_sin_iva","iva","precio_compra_con_iva","proveedor","proveedor_det","usuario_alta_det","usuario_modifica_det","variacion_list","activo","fecha_alta","fecha_modificacion")        
        read_only_fields = ["id,fecha_alta"]
        extra_kwargs = {"proveedor":{"write_only":True},"usuario_alta":{"write_only":True},"usuario_modifica":{"write_only":True}}
    
    def create(self,validate_data):
        instance = Articulo()
        
        instance.nombre = validate_data.get("nombre")
        instance.descripcion = validate_data.get("descripcion")
        instance.proveedor = validate_data.get("proveedor")
        instance.precio_compra_sin_iva = validate_data.get("precio_compra_sin_iva")
        instance.iva = validate_data.get("iva")
        instance.precio_compra_con_iva =  validate_data.get("precio_compra_con_iva")
        instance.usuario_alta = Token.objects.get(key = validate_data.get("token")).user
        instance.fecha_alta = timezone.now()
        instance.usuario_modifica = Token.objects.get(key = validate_data.get("token")).user
        instance.fecha_modificacion = timezone.now()
        instance.activo = "S"
        
        instance.save()
        return instance
    
    def update(self,instance,validate_data):
        
        instance.nombre = validate_data.get("nombre",instance.nombre)
        instance.descripcion = validate_data.get("descripcion",instance.descripcion)
        instance.proveedor = validate_data.get("proveedor",instance.proveedor)
        instance.precio_compra_sin_iva = validate_data.get("precio_compra_sin_iva",instance.precio_compra_sin_iva)
        instance.iva = validate_data.get("iva",instance.iva)
        instance.precio_compra_con_iva =  validate_data.get("precio_compra_con_iva",instance.precio_compra_con_iva)
        #usuario_alta = models.ForeignKey(User, on_delete=models.PROTECT,related_name = "usuario_alta")
        #fecha_alta = models.DateTimeField(auto_now_add=True)
        instance.usuario_modifica = Token.objects.get(key = validate_data.get("token")).user
        instance.fecha_modificacion = timezone.now()
        instance.activo = validate_data.get("activo",instance.activo)
        
        instance.save()
        return instance
    
        
        
