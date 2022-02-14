from rest_framework import serializers
from ..models.Proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Proveedor
        fields = ["id","descripcion","activo"]
        read_only_fields = ["id"]
    
    

