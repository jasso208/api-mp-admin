from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..serializers.ArticuloSerializer import ArticuloSerializer
from ..serializers.VariacionArticuloSerializer import VariacionArticuloSerializer
from ..models.Articulo import Articulo
from ..models.VariacionArticulo import VariacionArticulo
from  rest_framework import status
from ..clases_generales.response import ResponseGeneral

class ArticuloView():    
    @api_view(['GET','POST'])
    def articulo_list(request):
        response = ResponseGeneral()
        if request.method == "POST":
            serializer = ArticuloSerializer(data = request.data)
            
            token = request.META["HTTP_AUTHORIZATION"].replace("Token ","")   
            
            with transaction.atomic():
                if serializer.is_valid():
                    articulo = serializer.save(token = token)
                    
                    #Guardamoslas variaciones del producto
                    #Agregamos el nuevo articulo creado a las variaciones
                    for x in range(0,len(request.data["variacion_list"])):
                        request.data["variacion_list"][x]["articulo"] = articulo.id
                    
                    serializer_variacion = VariacionArticuloSerializer(data = request.data["variacion_list"],many=True)                
                    if(serializer_variacion.is_valid()):
                        serializer_variacion.save()
                    else:
                        transaction.set_rollback(True)
                        return Response(response.set_data_and_status(serializer_variacion.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
                    return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)
                else:
                    return Response(response.set_data_and_status(serializer.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
            
        elif request.method == "GET":
            articulo = Articulo.objects.all()
            serializer = ArticuloSerializer(articulo,many = True)
            return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)
    
    @api_view(["GET","PUT","DELETE"])  
    @transaction.atomic
    def articulo_detail(request,pk):
        
        response = ResponseGeneral()
        if request.method == "GET":
            
            try:
                articulo = Articulo.objects.get(id= pk)
            except:
                res = response.set_data_and_status({"error":"Artículo no encontrado"},"400")
                return Response(res,status = status.HTTP_404_NOT_FOUND)
            
            serializer = ArticuloSerializer(articulo)
                
            return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)
        
        if request.method == "PUT":
            try:
                articulo = Articulo.objects.get(id = pk)
            except:
                return Response(response.set_data_and_status({"error":"Artículo no encontrado"},"400"),status = status.HTTP_404_NOT_FOUND)
                
                
            token = request.META["HTTP_AUTHORIZATION"].replace("Token ","")   
            
            serializer = ArticuloSerializer(articulo,data = request.data)
            
            #serializer.data["usuario_modifica"] = Token.objects.get(key = token)
            
            
            with transaction.atomic():
                if serializer.is_valid():
                    articulo = serializer.save(token = token)
                    
                    #Eliminamos las variaciones actuales y agregamos las nuevas
                    VariacionArticulo.objects.filter(articulo = articulo).delete()
                    
                    for x in range(0,len(request.data["variacion_list"])):
                        request.data["variacion_list"][x]["articulo"] = articulo.id
                    
                    serializer_variacion = VariacionArticuloSerializer(data = request.data["variacion_list"],many = True)
                    if serializer_variacion.is_valid():
                        serializer_variacion.save()
                        return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)
                    else:     
                                         
                        transaction.set_rollback(True)
                        return Response(response.set_data_and_status(serializer_variacion.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
                        
                else:
                    transaction.set_rollback(True)
                    return Response(response.set_data_and_status(serializer.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
            
        if request.method == "DELETE":
            try:
                articulo = Articulo.objects.get(id = pk)
            except:
                return Response(response.set_data_and_status({"error":"Artículo no encontrado"},"400"),status = status.HTTP_404_NOT_FOUND)
            articulo.activo = "N"    
            articulo.save()
            return Response(response.set_data_and_status("ok","200"),status = status.HTTP_200_OK)
        