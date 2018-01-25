import random

def genAleatorio(dimVect):
	vectW = []
	for i in range(dimVect - 1):
		vectW.append(random.uniform(-1.0,1.0))
	print(vectW)
	return vectW