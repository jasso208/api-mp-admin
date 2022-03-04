from tokenize import Token
from rest_framework.decorators import api_view
from ..general_class.response import ResponseGeneral
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from ..serializers.user_serializer import UserSerializer

class UserView:
    
    @api_view(['GET'])
    def get_user_session(request):
        response = ResponseGeneral()
        if request.method == 'GET':
            try:
                user = Token.objects.get(key=request.GET.get("token")).user
                serializer = UserSerializer(user)
                return Response(response.set_data_and_status(serializer.data,"200"),status = status.HTTP_200_OK)
            except:
                return Response(response.set_data_and_status({"error":"Token incorrecto"},"400"),status = status.HTTP_404_NOT_FOUND)
        
    