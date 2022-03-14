from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..serializers.ProveedorSerializer import ProveedorSerializer
from ..models.Proveedor import Proveedor
from rest_framework.pagination import PageNumberPagination
from ..clases_generales.response import ResponseGeneral

class ProveedorView(ResponseGeneral):
    
    @api_view(['GET','POST'])
    def proveedor_list(request):
        response = ResponseGeneral()
        if request.method == 'POST':
            serializer = ProveedorSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)                
            else:
                return Response(response.set_data_and_status(serializer.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
                
                        
        elif request.method == 'GET':
            paginator = PageNumberPagination()
            paginator.page_size=request.GET.get("page_size")
            proveedor = Proveedor.objects.all().order_by("id")
            context = paginator.paginate_queryset(proveedor,request)
            serializer = ProveedorSerializer(context,many = True)
            return paginator.get_paginated_response(serializer.data)
        
    @api_view(['GET','DELETE','PUT'])
    def proveedor_detail(request,pk):
        response = ResponseGeneral()
        if request.method == 'PUT':
            try:
                proveedor = Proveedor.objects.get(id = pk)
            except:
                return Response(response.set_data_and_status({"error":"Proveedor no encontrado"},"400"),status = status.HTTP_404_NOT_FOUND)
            
            serializer = ProveedorSerializer(proveedor,data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)
            else:
                return Response(response.set_data_and_status(serializer.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
        
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
        