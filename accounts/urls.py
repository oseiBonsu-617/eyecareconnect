from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('register', views.RegisterView, basename='register')

urlpatterns = [
    path(r'', include(router.urls))
]
