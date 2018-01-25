### IMPORTACION DE FUNCIONES Y METODOS ###
import numpy
from aleatorio import aleatorio
from genAleatorio import genAleatorio
from extraerVector import extraerVector
### IMPORTACION DE FUNCIONES Y METODOS ###


### MENU ###
print("Escoja opcion:")
print("1. Metodo con Formulas")
print("2. Metodo Aleatorio")
op = int(input("Opcion: "))
while op <= 0 or op >= 3:
	op = int(input("Opcion: "))
if op == 2:
	aleatorio()
### MENU ###


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
vectW = []
for i in range(dimVect - 1):
	valor = float(input("Ingrese W[] Valor %d: " %(i+1)))
	vectW.append(valor)
### CREACION E INGRESO DE PESOS ###


### CREACION E INGRESO DEL UMBRAL ###
umbral = float(input("Ingrese Valor b (umbral): "))
### CREACION E INGRESO DEL UMBRAL ###


### DEFINICION DE LIMITE DE ITERACIONES ###
limIte = 1000
n = 0
### DEFINICION DE LIMITE DE ITERACIONES ###


### ITERACIONES ###
while n < limIte:
	for i in range(cantVect):
		print("###################")
		print("### ITERACION %d ###" %(n+1))
		print("###################")
		print("a = (W * p) + b")
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
		if(error == 0):
			break
		else:
			matW = matW + (error * numpy.transpose(matP))
			vectW = matW.A1.tolist()
		n = n + 1
	if(error == 0):
		break
### ITERACIONES ###
