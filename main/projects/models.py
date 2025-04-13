# projects/models.py
from django.db import models
from user.models import Developer, NGO
from skills.models import Skill

class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    skills_required = models.ManyToManyField(Skill, through='ProjectSkill')
    
    def __str__(self):
        return self.title

class ProjectSkill(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    importance_level = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        unique_together = ('project', 'skill')

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    application_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()
    expected_completion_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.developer.name} - {self.project.title}"