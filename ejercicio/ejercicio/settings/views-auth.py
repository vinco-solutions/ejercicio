from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

class Login(ObtainAuthToken):

    def post(self, request, *args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            print("Login successfuly")
        return Response({'message': 'Login successfuly'}, status = status.HTTP_200_OK)
