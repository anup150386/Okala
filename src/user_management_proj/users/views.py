from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import APIView
from .models import AppUser, Project
from .serializers import UserSerializer, ProjectSerializer


class UserViewSet(APIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serialized = self.serializer_class()
        return Response(serialized.data)

    def post(self, request, format=None):
        print(request.data)
        serialized = self.serializer_class(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serialized = self.serializer_class(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, format=None):
        serialized = self.serializer_class()
        return Response(serialized.data)

    def post(self, request, format=None):
        serialized = self.serializer_class(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

