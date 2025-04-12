# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CareerPath(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CareerSkillRelation(models.Model):
    career = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='careers')
    importance = models.IntegerField(default=5)  # Scale 1-10
    
    class Meta:
        unique_together = ('career', 'skill')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class UserSkill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.IntegerField(default=5)  # Scale 1-10
    
    class Meta:
        unique_together = ('user', 'skill')

class Resume(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='resumes')
    content = models.TextField()
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.user.username}'s resume - {self.created_at.strftime('%Y-%m-%d')}"

class InterviewPrep(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='interview_preps')
    role = models.CharField(max_length=100)
    tips = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.user.username}'s interview prep for {self.role}"