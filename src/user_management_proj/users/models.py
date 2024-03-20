from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point


# Custom imports

class Project(models.Model):
    """
    This class will contain all the information related to a project that has been assigned
    to a user.
    """
    project_uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    users = models.ManyToManyField('AppUser', related_name='user_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #geographic_info = models.PointField(default=Point(0, 0))

    def __str__(self):
        return f"Name : {self.name}, Description : {self.description}"

# Create your models here.
class AppUser(User):
    expertise = models.IntegerField(default=0)
    projects = models.ManyToManyField(Project, related_name='projects_users')


