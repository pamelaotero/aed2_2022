# Exercício
# 
# Imprimir, usando for, a sequência
# 
# 
# 11 12 13 14 15
# 21 22 23 24 
# 31 32 33
# 41 42
# 51

for l in range(1, 6):
    for c in range(1, 6 - l + 1):
        print(l * 10 + c, end=' ')
    print()
