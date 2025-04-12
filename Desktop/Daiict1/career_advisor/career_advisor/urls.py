"""
URL configuration for career_advisor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import home_view, career_paths_view, login_view, signup_view, forgot_password_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('career-paths/', career_paths_view, name='career_paths'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('', home_view, name='home'),
]