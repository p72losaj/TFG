"""
Definition of urls for TTFProyectDjango.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('tecnologias/', views.tecnologias, name='tecnologias'),
    path('tecnologias/Django/', views.dJango, name='Django'),
    
    #path('admin/', admin.site.urls),
]
