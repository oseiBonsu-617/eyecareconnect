from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsExaminerOrReadOnly

from .models import (
    Examination,
    VisualAcuity,
    Refraction,
    OcularAssessment
)
from .serializers import (
    ExaminationSerializer,
    VisualAcuitySerializer,
    RefractionSerializer,
    OcularAssessmentSerializer
)


# Create your views here.
class ExaminationViewSet(viewsets.ModelViewSet):
    serializer_class = ExaminationSerializer
    permission_classes = [permissions.IsAuthenticated, IsExaminerOrReadOnly]


    def get_queryset(self):
        queryset = Examination.objects.all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
    

    def perform_create(self, serializer):
        serializer.save(examiner=self.request.user)

    @action(detail=True, methods=["GET", "POST"])
    def visual_acuity(self, request, pk=None):
        exam = self.get_object()

        if request.method == "POST":
            if exam.examiner != request.user and request.user.role != "admin":
                return Response(
                    {"detail": "You do not have permission to modify this exam."},
                    status=403
                )
            if hasattr(exam, 'visual_acuity'):
                return Response(
                    {'detail': 'Visual acuity already exits for this exam.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = VisualAcuitySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(examination=exam)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if not hasattr(exam, 'visual_acuity'):
            return Response(
                {'detail': 'No visual acuity recorded yet.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VisualAcuitySerializer(exam.visual_acuity)
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET", "POST"])
    def refraction(self, request, pk=None):
        exam = self.get_object()

        if request.method == "POST":
            if exam.examiner != request.user and request.user.role != "admin":
                return Response(
                    {"detail": "You do not have permission to modify this exam."},
                    status=403
                )
            
            if hasattr(exam, "refraction"):
                return Response(
                    {"detail": "Refraction already exists for this exam."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer = RefractionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(examination=exam)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if not hasattr(exam, "refraction"):
            return Response(
                {"detail": "No refraction recorded yet."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RefractionSerializer(exam.refraction)
        return Response(serializer.data)
    
    

    @action(detail=True, methods=["GET", "POST"])
    def ocular_assessment(self, request, pk=None):
        exam = self.get_object()

        if request.method == "POST":
            if exam.examiner != request.user and request.user.role != "admin":
                return Response(
                    {"detail": "You do not have permission to modify this exam."},
                    status=403
                )
            if hasattr(exam, "ocular_assessment"):
                return Response(
                    {"detail": "Ocular assessment already exists for this exam."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer = OcularAssessmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(examination=exam)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if not hasattr(exam, "ocular_assessment"):
            return Response(
                {"detail": "No ocular assessment recorded yet."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OcularAssessmentSerializer(exam.ocular_assessment)
        return Response(serializer.data)


