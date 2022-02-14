from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..serializers.ProveedorSerializer import ProveedorSerializer
from ..models.Proveedor import Proveedor

class ProveedorView():
    
    @api_view(['GET','POST'])
    def proveedor_list(request):
        if request.method == 'POST':
            serializer = ProveedorSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
                        
        elif request.method == 'GET':
            proveedor = Proveedor.objects.filter(activo = "S")
            serializer = ProveedorSerializer(proveedor,many = True)
            return Response(serializer.data)
        
    @api_view(['GET','DELETE','PUT'])
    def proveedor_detail(request,pk):
        if request.method == 'PUT':
            try:
                proveedor = Proveedor.objects.get(id = pk)
            except:
                return Response({"error":"Proveedor no encontrado"},status = status.HTTP_404_NOT_FOUND)
            
            serializer = ProveedorSerializer(proveedor,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            try:
                proveedor = Proveedor.objects.get(id = pk)
            except:
                return Response({"error":"Proveedor no encontrado"},status = status.HTTP_404_NOT_FOUND)
            
            proveedor.delete()        
            return Response(status = status.HTTP_204_NO_CONTENT)
    
        elif request.method == "GET":
            try:
                proveedor = Proveedor.objects.get(id = pk)
            except:
                return Response({"error":"Proveedor no encontrado"},status = status.HTTP_404_NOT_FOUND)
        
            serializer = ProveedorSerializer(proveedor)
            return Response(serializer.data,status = status.HTTP_200_OK)
        