from django.urls import path, include
from .views import (
    AnalyticsRootView,
    OverviewAnalyticsView,
    ScreeningAnalyticsView,
    RefractiveErrorAnalyticsView,
    ClinicianActivityAnalyticsView,
)

urlpatterns = [
    path("", AnalyticsRootView.as_view()),
    path("overview/", OverviewAnalyticsView.as_view()),
    path("screening/", ScreeningAnalyticsView.as_view()),
    path("refractive-errors/", RefractiveErrorAnalyticsView.as_view()),
    path("clinicians/", ClinicianActivityAnalyticsView.as_view()),
]
