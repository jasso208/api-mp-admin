from rest_framework.decorators import api_view
from ..serializers.RegistrationSerializer import RegistrationSerializer
from inventario.clases_generales.response import ResponseGeneral
from rest_framework import status
from rest_framework.response import Response

class RegistrationView():
    
    @api_view(["POST"])
    def registration_view(request):
        
        response = ResponseGeneral()
        
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_201_CREATED)
        else:
            return Response(response.set_data_and_status(serializer.errors,"400"),status = status.HTTP_400_BAD_REQUEST)
        