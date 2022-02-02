# [ [a11, a12, a13],
#   [a21, a22, a23],
#   [a31, a32, a33] ]

def verifica_identidade(matriz):
	for linha in range(len(matriz)):
		for coluna in range(len(matriz[linha])):
			if (linha == coluna and matriz[linha][coluna] != 1):
				return False
			elif (linha != coluna and matriz[linha][coluna] != 0):
				return False
	return True

# matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

if __name__=="__main__":
	#print("Digite uma matriz: ")
	matriz = eval(input())
	if (verifica_identidade(matriz) == True):
		print("sim")
	else: 
		print("nao")