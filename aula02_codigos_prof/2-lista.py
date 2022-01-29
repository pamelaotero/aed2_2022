# Lista eh um tipo primitivo de dados em Python. O tipo de dados em si
# eh "list". Uma construcao como a seguinte eh uma literal de lista.
# Literais sao construcoes que aparecem no codigo que representam
# literalmente uma variavel de algum tipo de dados
lis = [1, 2, 3, 4]

# Lembre-se que variaveis sao referencias. Portanto a linha seguinte
# nao cria uma copia da lista, apenas faz com que "lis" e "lis2"
# referenciem a mesma lista
lis2 = lis

# A atribuicao a seguir altera o primeiro elemento da lista
lis2[0] = 42

# Tanto "lis[0]" quanto "lis2[0]" referenciam a mesma lista
# que foi modificada acima
print(lis[0])
print(lis[1])
print(lis[2])
print(lis[3])

