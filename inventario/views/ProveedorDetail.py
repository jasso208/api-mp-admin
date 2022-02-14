from rest_framework.views import APIView
from rest_framework import status
from ..models.Proveedor import Proveedor
from rest_framework.response import Response
from ..serializers.ProveedorSerializer import ProveedorSerializer

class ProveedorDetail(APIView):
    def get(self,request,pk):
        try:
            proveedor = Proveedor.objects.get(id = pk)
        except:
            return Response({"error":"Proveedor no encontrado."},status = status.HTTP_404_NOT_FOUND)
        
        serializer = ProveedorSerializer(proveedor)
        
        return Response(serializer.data,status = status.HTTP_200_OK)
    

    def put(self,request,pk):
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
        
    def delete(self,request,pk):
        try:
            proveedor = Proveedor.objects.get(id = pk)
        except:
            return Response({"error","Proveedor no encontrado"},status = status.HTTP_404_NOT_FOUND)
        
        proveedor.delete()        
        return Response(status = status.HTTP_204_NO_CONTENT)