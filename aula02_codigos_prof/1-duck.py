# Exemplo de Duck Typing em Python

# A funcao soma() tem dois parametros. Eles podem receber argumentos
# de quaisquer tipos. Durante a execucao, o intepretador nao verifica
# os tipos de dados dos argumentos, apenas tenta aplicar o operador "+"
# nas variaveis "x" e "y"
def soma(x, y):
	return x + y

print("soma(3, 5) =", soma(3, 5))
print("soma('hello', 'world') =", soma("hello", "world"))
print("soma(3, '5') =", soma(3, '5'))
