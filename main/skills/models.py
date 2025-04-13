# skills/models.py
from django.db import models
from user.models import Developer

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class DeveloperSkill(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='developer_skills')
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        unique_together = ('developer', 'skill')
        
    def __str__(self):
        return f"{self.developer.name} - {self.skill.name}"