# TFG

# Tutor: Nicolás Emilia Garcia Pedrajas. Correo electrónico: ma1gapen@uco.es

# Comandos interesantes en python:

1. Obtener la ruta de los datasets

  >> import os
  >> 
  >> separador = os.path.sep
  >> 
  >> dir = os.path.dirname(os.path.abspath(__name__))
  >> 
  >> dir_actual = separador.join(dir.split(separador)[:-1])
  >> 
  >> dir_actual = os.path.join(dir_actual, 'TTFProyectDjango')
  >> 
  >> dir_actual = os.path.join(dir_actual, 'misDatasets')
  >> 
  >> dataset_route =  os.path.join(dir_actual, dataset_name)
