"""
Definition of urls for TTFProyectDjango.
"""

# from datetime import datetime
from django.urls import path
# from django.contrib import admin
# from django.contrib.auth.views import LoginView, LogoutView
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
    path('MineriaDatos/Datasets/', views.Datasets, name='Datasets'),
    path('MineriaDatos/comandosPython/', views.comandosPython, name='comandosPython'),
    
    path('MineriaDatos/ObtencionDatos/', views.ObtencionDatos, name='ObtencionDatos'),
    path('MineriaDatos/ObtencionDatos/ArchivosCSV/', views.ArchivosCSV, name='ArchivosCSV'),
    path('MineriaDatos/ObtencionDatos/ArchivosARFF/', views.ArchivosARFF, name='ArchivosARFF'),
    
    path('MineriaDatos/LimpiezaDatos/', views.LimpiezaDatos, name='LimpiezaDatos'),
    path('MineriaDatos/LimpiezaDatos/SeleccionDatosInteres', views.SeleccionDatosInteres, name='SeleccionDatosInteres'),
    path('MineriaDatos/LimpiezaDatos/Outliers', views.Outliers, name='Outliers'),
    path('MineriaDatos/LimpiezaDatos/DatosNulos', views.DatosNulos, name='DatosNulos'),
    
    
    path('MineriaDatos/Algoritmos/', views.AlgoritmosMiningData, name='Algoritmos'),
    path('MineriaDatos/Algoritmos/ArbolDecision', views.ArbolDecision, name='ArbolDecision'),
    path('MineriaDatos/Algoritmos/KNN', views.KNN, name='KNN'),
    
    path('MineriaDatos/TransformacionDatos/', views.TransformacionDatos, name='TransformacionDatos'),
    
    path('MineriaDatos/EvaluacionResultados/', views.EvaluacionResultados, name='EvaluacionResultados'),
    
]
