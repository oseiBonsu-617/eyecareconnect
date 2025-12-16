from rest_framework.routers import DefaultRouter
from .views import PatientViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('profile', PatientViewSet, basename='patients')

urlpatterns = [
    path(r'', include(router.urls))
]
