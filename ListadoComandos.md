# Listado de comandos python

1. Enlaces datasets

  a) Iris Datasets: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/iris.data

2. Cargar fichero usando enlace

  >> import pandas as pd

  >> from pyodide.http import open_url
  
  >> url = 'url_dataset'
  
  >> dataset = pd.read_csv(open_url(url))
  
