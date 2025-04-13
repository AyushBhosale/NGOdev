# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUser already has first_name, last_name, email, password
    # date_of_birth = models.DateField(blank=True, null=True)
    pass

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='developer_profile')
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    experience = models.CharField(max_length=255)
    resume_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ngo_profile')
    organization_name = models.CharField(max_length=255)
    mission_statement = models.TextField()
    logo_url = models.ImageField(upload_to='ngo_logos/', blank=True, null=True)
    website = models.URLField(blank=True)
    year_founded = models.CharField(max_length=4)
    size = models.CharField(max_length=50)
    verification_status = models.CharField(max_length=50, default='Pending')
    
    def __str__(self):
        return self.organization_name