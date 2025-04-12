from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import career_advice_api, career_paths_api

# Create a router
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # Add the career advice API endpoint
    path('career-advice/', career_advice_api, name='career_advice_api'),
    # Add career paths API endpoint
    path('career-paths/', career_paths_api, name='career_paths_api'),
]