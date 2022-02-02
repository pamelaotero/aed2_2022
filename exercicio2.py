# Criação da lista
lista = []
# Definindo o tamanho da lista conforme a questão
tam = 10

# Fazendo a interação
for i in range(tam):
     valor = int(input(''))
     lista.append(valor) # Adicionando elemento na lista

print(min(lista), max(lista))