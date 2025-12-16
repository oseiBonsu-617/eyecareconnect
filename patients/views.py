from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    search_fields = ['first_name', 'last_name', 'contact']
    ordering_fields = ['first_name', 'last_name']
    permission_classes = [IsAuthenticated]
    


    # # Add a method to handle GET requests
    # def get(self, request, *args, **kwargs):
    #     return Response({"message": "Register form (or page) is here"}, status=200)
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (patient, created) = Patient.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PatientSerializer(patient, data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)