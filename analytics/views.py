from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsClinicianOrAdmin

from .services import (
    get_overview_stats,
    get_screening_stats,
    get_refractive_error_stats,
    get_clinician_activity,
)

class AnalyticsRootView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "overview": "/analytics/overview/",
            "screening": "/analytics/screening/",
            "refractive_errors": "/analytics/refractive-errors/",
            "clinicians": "/analytics/clinicians/",
        })

# Create your views here.
class OverviewAnalyticsView(APIView):
    permission_classes = [IsClinicianOrAdmin]

    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        data = get_overview_stats(start_date, end_date)
        return Response(data)
    

class ScreeningAnalyticsView(APIView):
    permission_classes = [IsClinicianOrAdmin]

    def get(self, request):
        data = get_screening_stats()
        return Response(data)

class RefractiveErrorAnalyticsView(APIView):
    permission_classes = [IsClinicianOrAdmin]

    def get(self, request):
        data = get_refractive_error_stats()
        return Response(data)

class ClinicianActivityAnalyticsView(APIView):
    permission_classes = [IsClinicianOrAdmin]

    def get(self, request):
        data = list(get_clinician_activity())
        return Response(data)
