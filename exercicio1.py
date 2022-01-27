# Entre com o tamanho da lista

tam = int(input(''))

# Entre com os elementos da lista separados por espaço
input_string = input('')

lista = input_string.split()

# imprimindo a lista
print('lista: ', lista)

# converte os valores da lista para inteiro
for i in range(tam):
  lista[i] = int(lista[i])

lista.reverse()

print(lista)

