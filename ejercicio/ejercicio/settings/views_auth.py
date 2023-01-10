from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class Login(ObtainAuthToken):

    def post(self, request, *args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user = user)
            if created:
                return Response ({'token': token.key, 'message': 'Login successfuly'}, status=status.HTTP_201_CREATED)
            else:
                token.delete()
                token = Token.objects.create(user = user)
                return Response ({'token': token.key, 'message': 'Login successfuly'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'You have entered incorrect username or password'})
        return Response({'message': 'Login successfuly'}, status = status.HTTP_200_OK)
