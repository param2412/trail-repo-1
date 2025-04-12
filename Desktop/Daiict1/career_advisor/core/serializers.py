from rest_framework import serializers
from .models import CareerPath, Skill, UserProfile, UserSkill, Resume, InterviewPrep

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CareerPathSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    
    class Meta:
        model = CareerPath
        fields = ['id', 'name', 'description', 'skills']
    
    def get_skills(self, obj):
        career_skills = obj.skills.all()
        return [{'id': cs.skill.id, 'name': cs.skill.name, 'importance': cs.importance} 
                for cs in career_skills]

class UserSkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField(source='skill.name', read_only=True)
    
    class Meta:
        model = UserSkill
        fields = ['id', 'skill', 'skill_name', 'proficiency']

class UserProfileSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'bio', 'skills']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'content', 'feedback', 'created_at']

class InterviewPrepSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewPrep
        fields = ['id', 'role', 'tips', 'created_at']