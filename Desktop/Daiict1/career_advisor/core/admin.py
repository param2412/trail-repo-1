# from django.contrib import admin

# # Register your models here.
from django.contrib import admin
from .models import (
    CareerPath, Skill, CareerSkillRelation, 
    UserProfile, UserSkill, Resume, InterviewPrep
)

admin.site.register(CareerPath)
admin.site.register(Skill)
admin.site.register(CareerSkillRelation)
admin.site.register(UserProfile)
admin.site.register(UserSkill)
admin.site.register(Resume)
admin.site.register(InterviewPrep)
