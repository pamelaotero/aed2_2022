# Um exemplo com leitura do teclado
#
# A funcao input() le uma linha inteira do teclado. A sequencia de caracteres
# lidos eh uma string. Essa string pode ser interpretada como uma variavel
# do tipo "int" se for passada como argumento para "int()"
print("Quantos elementos o vetor deve ter?")
num_elementos = int(input())

if num_elementos > 10:
    print("O numero de elementos deve ser no maximo 10")

# Uma forma conveniente de criar uma lista que contem um certo numero de
# elementos eh concatenar a lista "[0]" varias vezes. Podemos fazer isso
# com "[0] + [0] + ... + [0]" ou usando o operador "*"
lis = [0] * num_elementos
for i in range(num_elementos):
    print("Digite o elemento n", i + 1)
    lis[i] = int(input())

# Daqui pra frente eh apenas um laco de repeticao e uma variavel acumuladora
soma = 0
for x in lis:
    soma += x

print("A soma dos elementos eh", soma)
