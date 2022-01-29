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
# Execute este programa e digite o seguinte no teclado (em uma linha so):
#
#    [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
#
# A funcao "input()" vai ler essa sequencia de caracteres e passar
# para a funcao "eval()". A funcao "eval()" vai transformar isso em
# uma lista de listas


def le_lista():
    print("Digite uma matriz PAMELAO")
    matriz = eval(input())
    # [ [a11, a12, a13],
    #   [a21, a22, a23],
    #   [a31, a32, a33] ]
    for linha in matriz:
        for elem in linha:
              
            print(elem, end=' ')
        print()
if __name__=="__main__":
    le_lista()


