from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .serializers import UserSerializer, ProjectSerializer


class TestUserSerializer(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_data = {
            'username': 'testuser',
            'email': '<EMAIL>',
            'password': 'password'
        }

    def test_create_user(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])

    def test_create_user_missing_field(self):
        serializer = UserSerializer(data={
            'username': 'testuser',
            'email': '<EMAIL>'
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'password': ['<PASSWORD>.']}
        )

    def test_create_user_invalid_email(self):
        serializer = UserSerializer(data={
            'username': 'testuser',
            'email': 'test@',
            'password': 'password'
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'email': ['Enter a valid email address.']}
        )


class TestProjectSerializer(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.project_data = {
            'name': 'Test Project',
            'description': 'This is a test project.'
        }

    def test_create_project(self):
        serializer = ProjectSerializer(data=self.project_data)
        self.assertTrue(serializer.is_valid())
        project = serializer.save()
        self.assertEqual(project.name, self.project_data['name'])
        self.assertEqual(
            project.description,
            self.project_data['description']
        )

    def test_create_project_missing_field(self):
        serializer = ProjectSerializer(data={
            'name': 'Test Project'
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'description': ['This field is required.']}
        )

    def test_create_project_invalid_name(self):
        serializer = ProjectSerializer(data={
            'name': 'Test Project!',
            'description': 'This is a test project.'
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'name': ['Enter a valid '
                      'identifier. '
                      'This value may contain only letters, numbers, underscores or hyphens.']}
        )