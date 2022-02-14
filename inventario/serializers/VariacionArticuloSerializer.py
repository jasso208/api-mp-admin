
from rest_framework import serializers
from ..models.VariacionArticulo import VariacionArticulo
from ..serializers.ColorSerializer import ColorSerializer

class VariacionArticuloSerializer(serializers.ModelSerializer):
        color_detail = ColorSerializer(read_only = True,source = "color")
        class Meta:
            model = VariacionArticulo
            fields = ["id","articulo","color","color_detail"]
            extra_kwargs = {"color":{"write_only":True},"articulo":{"write_only":True}}
            