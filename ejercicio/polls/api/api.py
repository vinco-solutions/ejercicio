from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from polls.api.serializers import question_serializer, UserSerializer, RegisterSerializer, LoginSerializer
from knox.models import AuthToken



class question_get_delete(generics.RetrieveDestroyAPIView):
    '''
    Read or delete a single model instance 
    '''
    serializer_class = question_serializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

class question_create(generics.CreateAPIView):
    '''
    Create a single model instance 
    '''
    serializer_class = question_serializer

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Question created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class question_update_delete(generics.RetrieveUpdateDestroyAPIView):
    '''
    Read or delete a single model instance 
    '''
    serializer_class = question_serializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

# =============================================================================
# User actions
# =============================================================================

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user,context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
            })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            'user': UserSerializer(user,context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
            })

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



# # Exposure Annotations Viewset
# class AbstractExposureAnnotationViewSet(GenericMultipleAnnotationsViewSet):
#     # Setup
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]


#     def get_queryset(self):
#         return self.request.user.exposures_annotations.all()

