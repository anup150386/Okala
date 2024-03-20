from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProjectSerializer
from .models import User, Project

class UserViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serialized = self.serializer_class()
        return Response(serialized.data)


class ProjectViewSet(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, format=None):
        serialized = self.serializer_class()
        return Response(serialized.data)

