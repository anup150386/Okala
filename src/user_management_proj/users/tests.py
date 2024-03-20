import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import User
from .serializers import UserSerializer


@pytest.mark.django_db
def test_project_model():
    project = Project(
        name="Test Project",
        description="This is a test project",
        status="In Progress",
        users=[],
    )
    project.save()

    retrieved_project = Project.objects.get(name="Test Project")

    assert retrieved_project.name == "Test Project"
    assert retrieved_project.description == "This is a test project"
    assert retrieved_project.status == "In Progress"
    assert retrieved_project.users == []
    #assert retrieved_project.geographic_info == Point(0, 0)


from django.test import TestCase
from rest_framework.test import APIRequestFactory
from.models import Project
from.views import ProjectViewSet

class ProjectViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ProjectViewSet.as_view({'get': 'get'})
        self.project = Project.objects.create(title='Project 1')

    def test_get_method(self):
        request = self.factory.get('/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {
                'id': self.project.id,
                'title': 'Project 1'
            }
        ])





class UserViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_url = reverse("user-list")
        self.user_data = {"username": "testuser", "email": "<EMAIL>"}
        self.user = User.objects.create_user(**self.user_data)

    def test_get_users(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(self.user).data)