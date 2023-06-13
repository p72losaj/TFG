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
        'app/index.html'
    )

def tecnologias(request):
    """Renders the tecnologias page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias.html'
    )


def MineriaDatos(request):
    "Renders the Mineria de datos page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MineriaDatos.html',
        {
            'title':'Mineria de datos',
            'message':'Pagina de descripcion de mineria de datos',
        }
    )

def simuladorPython(request):
    "Renders the comandosPython/ page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/simuladorPython.html'
    )