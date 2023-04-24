# Dataset iris

1. Url: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/iris.data
2. Caracteristicas iris = ["sepal length","sepal width","petal length","petal width","class"]

# Comandos python

1. Cargar fichero usando enlace

  >> import pandas as pd

  >> from pyodide.http import open_url
  
  >> url = 'url_dataset'
  
  >> dataset = pd.read_csv(open_url(url))
  
