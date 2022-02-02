# criando a lista
lista = []

# entrando com o tamanho da lista
tam = int(input(""))

# iterando até o intervalo 
for i in range(0, tam):
  valor = int(input())
  lista.append(valor) # adicionando elemento na lista

# print(lista)
lista.reverse()
print(lista)