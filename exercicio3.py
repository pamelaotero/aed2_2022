# A funcao "eval()" pode ser usada para interpretar uma expressao como se
# fosse codigo em Python
#
# Se fizermos, por exemplo, o seguinte...
#
#     x = eval('5 + 3 * 2')
#
# o resultado vai ser que a variável "x" terá o valor 30 e tipo "int".
#
# Se a expressao contiver uma lista ou uma lista de lista, entao a funcao
# "eval()" pode gerar uma lista ou uma matriz.
#
# Execute este programa e digite o seguinte no teclado (em uma i so):
#
#    [[10, 0, 0], [0, 1, 0], [0, 0, 1]]
#
# A funcao "input()" vai ler essa sequencia de caracteres e passar
# para a funcao "eval()". A funcao "eval()" vai transformar isso em
# uma lista de listas

    # [ [a11, a12, a13],
    #   [a21, a22, a23],
    #   [a31, a32, a33] ]

# def verifica_identidade(matriz):
#     for linha in range(len(matriz)):
#         for j in linha:
#             if (linha == coluna and matriz[linha][coluna] != 0):
#                 return False
#     return True

matriz = [[10, 0, 0,0], [0, 0,1, 0], [0, 0,0, 1]]

# for linha in range(len(matriz)):
#   for coluna in range(len(matriz[linha])):
#   	if (linha == coluna a)
#     print(matriz[linha][coluna])
#   print()

if __name__=="__main__":
    print("Digite uma matriz: ")
    matriz = eval(input())
    print("----------- Printando a matriz ------------")
    for linha in matriz:
        for elem in linha:
            print(elem, end=' ')
        print()
    print("----- Identificando se é Identidade -------")
    if (verifica_identidade(matriz) == True):
        print("a diagonal principal esta prenchida com 1")
    else: 
        print("nao entrou")




