import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


#from django.contrib.gis.geos import Point


# Custom imports

class Project(models.Model):
    """
    This class will contain all the information related to a project that has been assigned
    to a user.
    """
    project_uuid = models.UUIDField(default=uuid.uuid4()) # The ID should be the primary key not this one
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    users = models.ManyToManyField('AppUser')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #geographic_info = models.PointField(default=Point(0, 0)) # Facing issue in installing the library, but it will be done
    geographic_info = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Name : {self.name}, Description : {self.description}"


class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    expertise = models.IntegerField(default=0)
    projects = models.ManyToManyField(Project, blank=True, null=True)


