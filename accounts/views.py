from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from django.shortcuts import render
from .serializers import UserCreateSerializer

User = get_user_model()

# Create your views here.
class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer