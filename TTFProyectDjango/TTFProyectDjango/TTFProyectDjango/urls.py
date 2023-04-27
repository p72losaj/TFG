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
    path('tecnologias/html/', views.html, name='html'),
    path('tecnologias/JavaScript/', views.JavaScript, name='JavaScript'),
    path('tecnologias/CSS/', views.CSS, name='CSS'),
    path('tecnologias/Python/', views.Python, name='Python'),
    path('tecnologias/Bash/', views.Bash, name='Bash'),
    path('MineriaDatos/', views.MineriaDatos, name='MineriaDatos'),
    path('MineriaDatos/ObtencionDatos/', views.ObtencionDatos, name='ObtencionDatos'),
    path('MineriaDatos/ObtencionDatos/ArchivosCSV/', views.ArchivosCSV, name='ArchivosCSV'),
    path('MineriaDatos/ObtencionDatos/ArchivosARFF/', views.ArchivosARFF, name='ArchivosARFF'),
    path('MineriaDatos/LimpiezaDatos/', views.LimpiezaDatos, name='LimpiezaDatos'),
    path('MineriaDatos/Algoritmos/', views.AlgoritmosMiningData, name='Algoritmos'),
    path('MineriaDatos/TransformacionDatos/', views.TransformacionDatos, name='TransformacionDatos'),
    path('MineriaDatos/EvaluacionResultados/', views.EvaluacionResultados, name='EvaluacionResultados'),
    path('simuladorPython/', views.simuladorPython, name='simuladorPython'),
    path('simuladorPython/Datasets/', views.Datasets, name='Datasets'),
    path('simuladorPython/comandosPython/', views.comandosPython, name='comandosPython'),
    path('MineriaDatos/ObtencionDatos/ArchivosCSV/Ejercicios/', views.EjerciciosCSV, name='EjerciciosCSV'),
    #path('admin/', admin.site.urls),
]
