# Agora, em vez de fazer com que "lis2" seja uma referencia para a mesma
# lista referenciada por "lis", vamos fazer uma copia
lis = [1, 2, 3, 4]
lis2 = list(lis)

# Temos duas listas em memoria. Apenas aquela referenciada por "lis2"
# vai ser alterada na linha a seguir
lis2[0] = 42

print("lis")
print(lis[0])
print(lis[1])
print(lis[2])
print(lis[3])

print("lis2")
print(lis2[0])
print(lis2[1])
print(lis2[2])
print(lis2[3])

