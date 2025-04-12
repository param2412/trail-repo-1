from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_career_advice

def home_view(request):
    """View for home page"""
    return render(request, 'home.html')

def career_paths_view(request):
    """View for career paths page with Q&A"""
    return render(request, 'career_paths.html')

def login_view(request):
    """View for login page"""
    return render(request, 'login.html')

def signup_view(request):
    """View for signup page"""
    return render(request, 'signup.html')

def forgot_password_view(request):
    """View for forgot password page"""
    return render(request, 'forgot_password.html')

@api_view(['GET'])
def career_paths_api(request):
    """API endpoint for listing career paths"""
    # This is a placeholder - in a real app, you'd fetch from your database
    career_paths = [
        {
            "id": 1,
            "name": "Software Development",
            "description": "Design, develop, and maintain software applications and systems.",
            "skills": ["Programming", "Problem Solving", "Software Design"]
        },
        {
            "id": 2,
            "name": "Data Science",
            "description": "Extract insights and knowledge from structured and unstructured data.",
            "skills": ["Statistics", "Machine Learning", "Python", "Data Visualization"]
        },
        {
            "id": 3,
            "name": "UX/UI Design",
            "description": "Create user-friendly interfaces and experiences for digital products.",
            "skills": ["Design Thinking", "Wireframing", "User Research", "Visual Design"]
        },
        {
            "id": 4,
            "name": "Cybersecurity",
            "description": "Protect systems, networks, and data from digital attacks.",
            "skills": ["Network Security", "Penetration Testing", "Security Analysis"]
        },
        {
            "id": 5,
            "name": "Cloud Computing",
            "description": "Design and manage cloud infrastructure and services.",
            "skills": ["AWS/Azure/GCP", "Infrastructure as Code", "Containerization"]
        },
        {
            "id": 6,
            "name": "Business Management",
            "description": "Plan, coordinate, and direct organizational operations and strategic initiatives.",
            "skills": ["Leadership", "Strategic Planning", "Financial Acumen", "Communication"]
        }
    ]
    return Response(career_paths)

@api_view(['POST'])
def career_advice_api(request):
    """API endpoint for Career Q&A using AI"""
    question = request.data.get('question', '')
    
    if not question:
        return Response({'error': 'Question is required'}, status=400)
    
    # Get advice from AI service
    ai_response = get_career_advice(question)
    
    if ai_response.get('success'):
        return Response({'response': ai_response['response']})
    else:
        return Response({
            'error': 'Error getting advice from AI',
            'details': ai_response.get('error', 'Unknown error')
        }, status=500)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import career_advice_api, career_paths_api

# Create a router for REST API endpoints
router = DefaultRouter()
# If you have any ViewSets, register them here
# router.register('example', ExampleViewSet)

# URL patterns
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    
    # Add your API endpoint for career advice
    path('career-advice/', career_advice_api, name='career_advice_api'),
    path('career-paths/', career_paths_api, name='career_paths_api'),
]