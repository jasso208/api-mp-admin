from rest_framework import serializers
from ..models.Color import Color
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        
        