# TFG

# Tutor: Nicolás Emilia Garcia Pedrajas. Correo electrónico: ma1gapen@uco.es

# Comandos interesantes en python:

1. Obtener la ruta de los datasets

  >> import pandas as pd
  >> from pyodide.http import open_url
  >> url = 'rutaURL'
  >> df = pd.read_csv(open_url(url))
