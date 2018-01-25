def extraerVector(matrizPesos, i, dimVect):
	vectTemp = []
	for j in range(dimVect - 1):
		vectTemp.append(matrizPesos[i][j])
	return vectTemp