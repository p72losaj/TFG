"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Bienvenido a Nettlaer',
            'message':'Descripcion de la aplicacion web NETTLAERER',
        }
    )

def tecnologias(request):
    """Renders the language page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/tecnologias.html',
        {
            'title':'Tecnologias',
            'message':'Listado de tecnologias empleadas durante la realizacion del proyecto',
        }
    )

def dJango(request):
    "Renders the dJango page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/DJango.html',
        {
            'title':'Tecnologias-Django',
            'message':'Pagina de descripcion de la tecnologia Django',
        }
    )

def html(request):
    "Renders the html page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/html.html',
        {
            'title':'Tecnologias-HTML',
            'message':'Pagina de descripcion de la tecnologia HTML',
        }
    )

def JavaScript(request):
    "Renders the JavaScript page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/JavaScript.html',
        {
            'title':'Tecnologias-JAVASCRIPT',
            'message':'Pagina de descripcion de la tecnologia JavaScript',
        }
    )

def CSS(request):
    "Renders the CSS page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/CSS.html',
        {
            'title':'Tecnologias-CSS',
            'message':'Pagina de descripcion de la tecnologia CSS',
        }
    )

def Python(request):
    "Renders the Python page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/Python.html',
        {
            'title':'Tecnologias-Python',
            'message':'Pagina de descripcion de la tecnologia Python',
        }
    )

def Bash(request):
    "Renders the Bash page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias/Bash.html',
        {
            'title':'Tecnologias-Bash',
            'message':'Pagina de descripcion de la tecnologia Bash',
        }
    )

def MineriaDatos(request):
    "Renders the Mineria de datos page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/MineriaDatos.html',
        {
            'title':'Mineria de datos',
            'message':'Pagina de descripcion de mineria de datos',
        }
    )

def ObtencionDatos(request):
    "Renders the MiningData/ObtencionDatos page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/ObtencionDatos/ObtencionDatos.html',
        {
            'title':'Obtencion de Datos',
            'message':'Pagina de descripcion de obtención de datos en mineria de datos',
        }
    )

def ArchivosCSV(request):
    "Renders the MiningData/ObtencionDatos/ArchivosCSV page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/ObtencionDatos/ArchivosCSV.html',
        {
            'title':'Archivos CSV',
            'message':'Pagina de descripcion de archivos CSV en minería de datos',
        }
    )

def ArchivosARFF(request):
    "Renders the MiningData/ObtencionDatos/ArchivosARFF page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/ObtencionDatos/ArchivosARFF.html',
        {
            'title':'Archivos ARFF',
            'message':'Pagina de descripcion de archivos ARFF en minería de datos',
        }
    )

def LimpiezaDatos(request):
    "Renders the MiningData/LimpiezaDatos page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/LimpiezaDatos.html',
        {
            'title':'Mineria de datos-Limpieza de Datos',
            'message':'Pagina de descripcion de limpieza de datos en mineria de datos',
        }
    )

def TransformacionDatos(request):
    "Renders the MiningData/TransformacionDatos page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/TransformacionDatos.html',
        {
            'title':'Mineria de datos-Transformacion de Datos',
            'message':'Pagina de descripcion de transformacion de datos en mineria de datos',
        }
    )

def AlgoritmosMiningData(request):
    "Renders the MiningData/Algoritmos page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/AlgoritmosMiningData.html',
        {
            'title':'Mineria de datos-Algoritmos',
            'message':'Pagina de descripcion de algoritmos de mineria de datos',
        }
    )

def EvaluacionResultados(request):
    "Renders the MiningData/EvaluacionResultados page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos/EvaluacionResultados.html',
        {
            'title':'Mineria de datos-Evaluacion de Resultados',
            'message':'Pagina de descripcion de evaluacion de los resultados obtenidos al aplicar algoritmos de mineria de datos',
        }
    )


