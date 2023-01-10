from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from polls.api.serializers import question_serializer



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

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects






