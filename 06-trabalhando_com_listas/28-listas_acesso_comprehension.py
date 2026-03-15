numeros = [1, 20, 21, 2, 9, 65, 34]
pares=[]
quadrado = []

# Métodos simples
for num in numeros:
    if num % 2 ==0:
        pares.append(num)
print(pares)

for num in numeros:
    quadrado.append(num ** 2)
print(quadrado)
print()

# Método comprehension
pares2 = [num for num in numeros if num % 2 == 0]
quadrado2 = [num ** 2 for num in numeros ]

print(pares2)
print(quadrado2)