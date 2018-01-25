import numpy
import random
import sys
sys.path.append('./funciones')
sys.path.append('./aleatorio')
from extraerVector import extraerVector
from genAleatorio import genAleatorio

def aleatorio():
	### VALIDACIONES ###
	cantVect = int(input("Cantidad de Pesos (Min 2 & Max 10): "))
	dimVect = int(input("Ingrese dimension de vector peso (Max 3): "))
	dimVect = dimVect + 1
	### VALIDACIONES ###


	### CREACION MATRIZ DE PESOS ###
	matrizPesos = []
	for i in range(cantVect):
		matrizPesos.append([0] * dimVect)
	### CREACION MATRIZ DE PESOS ###


	### INGRESO DE VALORES ###
	for i in range(cantVect):
		for j in range(dimVect):
			if j == dimVect - 1:
				valor = int(input("Ingrese T%d: " %(i+1)))
				matrizPesos[i][j] = valor
				continue
			valor = int(input("Ingrese valor binario P%d (M[%d,%d]): " %((i+1),i,j)))
			matrizPesos[i][j] = valor

	print(matrizPesos)
	### INGRESO DE VALORES ###


	### CREACION E INGRESO DE PESOS ###
	vectW = genAleatorio(dimVect)
	### CREACION E INGRESO DE PESOS ###


	### CREACION E INGRESO DEL UMBRAL ###
	umbral = float("{0:.2f}".format(random.uniform(-1.0,1.0))) * 1.0
	### CREACION E INGRESO DEL UMBRAL ###


	### DEFINICION DE LIMITE DE ITERACIONES ###
	limIte = 10000
	n = 0
	### DEFINICION DE LIMITE DE ITERACIONES ###


	### ITERACIONES ###
	while n < limIte:
		for i in range(cantVect):
			print("###################")
			print("### ITERACION %d ###" %(n+1))
			print("###################")
			print("a umbral= (W * p) + b")
			matW = numpy.matrix(vectW)
			matP = numpy.transpose(numpy.matrix(extraerVector(matrizPesos, i, dimVect)))
			a = matW * matP
			a = float(a[0]) + float(umbral)
		
			if a >= umbral:
				print("a = %f	;	%f >= %f	; a = 1" %(a,a,umbral))
				a = float(1)
			else:
				print("a = %f	;	%f < %f	; a = 0" %(a,a,umbral))
				a = float(0)

			t = matrizPesos[i][dimVect-1]
			error = float(t - a)
			print("Error = t - a = %f" %error)
			print("Matriz de pesos: ",matW)
			print("Umbral = %f" %umbral)
			print("Iteracion: %d" %n)
			if(error == 0):
				break
			else:
				matW = matW + (error * numpy.transpose(matP))
				vectW = matW.A1.tolist()
				umbral = float(umbral + error)
			n = n + 1
		if(error == 0):
			break
	### ITERACIONES ###
	exit()