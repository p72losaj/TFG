#!/bin/python3

# Autor: Jaime Lorenzo Sanchez
# Version: 1.0
# Python version
try:
	import sys
	if (sys.version_info <= (3, 10)):
		print("Es necesaria una version de python 3.10 o superior")
		exit()
except ImportError:
	print("Modulo sys no instalado")
	exit()

# Modulo pandas

try:
	import pandas as pd
except ImportError:
	print("Modulo pandas no instalado")
	exit()

# Read dataset

def readDataset(url,colNames):
	dataset = pd.read_csv(url,header=None,names=colNames)
	return dataset

# Main Function
def main():
	print("Ejercicio. Obtenga al menos 10 conjuntos de datos en formato CSV")
	iris = readDataset("https://raw.githubusercontent.com/p72losaj/Introduccion_Mineria_Datos/main/PRACTICAS/misDatasets/iris.data",
				["sepal length","sepal width","petal length","petal width","Species"])
	print(iris.head())	

if __name__ == "__main__":
	main()

