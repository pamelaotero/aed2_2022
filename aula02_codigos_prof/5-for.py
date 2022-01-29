# Um laco de repeticao com iteradores
#
# O que o laco "for" faz eh modficar o valor da variavel iteradora. Em cada
# passo do laco de repeticao, a variavel iteradora referencia um elemento
# diferente da colecao

for i in [1,2,3,4,5,6,7,9,10]:
	print(i ,end=" ")
print()

# Uma expressao com "range" cria uma colecao que pode ser usada no lugar
# de uma lista. O comportamento de range() depende de quantos argumentos
# ela recebe.

# Um argumento: simboliza o limite superior da sequencia (aberto)
# range(n) --> [0, 1, 2, ..., n -1]
for i in range(11):
	print(i ,end=" ")
print()

# Dois argumentos: um eh o limite inferior (fechado) e outro eh o limite
# superior (aberto)
# range(n, m) --> [n, n+1, n+2, ..., m-1]
for i in range(1, 11):
	print(i ,end=" ")
print()

# Tres argumentos: alem especifica o limite inferior (fechado), o limite 
# superior (aberto) e o "passo"
# range(n, m, k) --> [n, n+k, n+2k, ..., n+xk]   (n+xk <= m)
for i in range(1, 11, 2):
	print(i ,end=" ")
print()

# Se o passo for negativo, os limites inferior e superior sao trocados.
# Agora eh o limite inferior que esta aberto. O laco de repeticao abaixo
# vai imprimir a sequencia decrescente 10, 9, ..., 2
# range(n, m, k) --> [n, n+k, n+2k, ..., n+xk]   (n+xk <= m)
for i in range(10, 1, -1):
	print(i ,end=" ")
print()
