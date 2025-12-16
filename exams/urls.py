from rest_framework.routers import DefaultRouter
from .views import ExaminationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('exams', ExaminationViewSet, basename='exams')

urlpatterns = [
    path(r'', include(router.urls)),
]
