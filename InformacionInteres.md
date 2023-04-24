# Iris Dataset

1. Url: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/iris.data
2. Caracteristicas iris dataset = ["sepal length","sepal width","petal length","petal width","class"]

# Wine Dataset

1. Url: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/abalone.data
2. Caracteristicas wine dataset = ['class', 'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 'Total_phenols','Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins', 'Color_intensity', 'Hue', 'OD280/OD315','Proline'])


# Diabetes Dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/diabetes.csv
2. Caracteristicas Dataset = ['preg', 'plas','pres','skin','insu','mass','pedi','age','class']

# Breast Cancer Dataset

1. Comando python: datasets.load_breast_cancer()

# Titanic Dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/titanic.csv

# Abalone Dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/abalone.data
2. Caracteristicas Dataset = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

# ildp dataset

1. Train Dataset URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/train_ildp.csv
2. Test Dataset URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/test_ildp.csv

# Digits dataset

1. URL: datasets.load_digits()

# Segment Challenge Dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/segment-challenge.arff

# Glass Dataset

1. URL : https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/glass.arff

# Dry Bean dataset

1. Url: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/Dry_Bean_Dataset.arff

# Car dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/car.data
2. Caracteristicas Dataset = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

# Zoo dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/zoo.data
2. Caracteristicas Dataset = ['animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airzorne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'class_type']

# Balance Scale Dataset

1. URL: https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/balance-scale.data
2. Caracteristicas Dataset = ['class_name', 'left_weight', 'left_distance', 'right_weight', 'right_distance']

# Comandos python

1. Cargar ficheros

  >> import pandas as pd
  >> from sklearn import datasets
  >> from scipy.io import arff
  >> from pyodide.http import open_url
  >> url = 'url_dataset'
  >> dataset = pd.read_csv(open_url(url))
  >> 


