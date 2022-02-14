from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..serializers.ProveedorSerializer import ProveedorSerializer
from ..models.Proveedor import Proveedor

class ProveedorList(APIView):
    
    def get(self,request):
        proveedor = Proveedor.objects.filter(activo = "S")
        serializer = ProveedorSerializer(proveedor,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProveedorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    @api_view()
    def get_all(self):
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor,many = True)
        return Response(serializer.data)
        

        
    
            