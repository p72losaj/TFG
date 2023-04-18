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
            'title':'Inicio',
            'message':'Descripcion de la aplicacion web NETTLAERER',
        }
    )

def tecnologias(request):
    """Renders the language page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tecnologias.html',
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
        'app/DJango.html',
        {
            'title':'Tecnologias-Django',
            'message':'Pagina de descripcion de la tecnologia Django',
        }
    )



