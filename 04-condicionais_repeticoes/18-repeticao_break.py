# loop infinito para testar o break
while True:
    numero = int(input('\nInforme um numero: '))

    if numero == 10:
        break

    print(numero, end=" ")

# Break com o for
print('\nUso do Break no for - range iria até 30, mas para no 11 (12 não é incluso)')
for numero in range(30):

    if numero == 12:
        break

    print(numero, end=" ")


# Continue com for - serve para "pular" a condição específica
print('\n\nUso do Continue no for - pula o numero 12')
for numero in range(30):

    if numero == 12:
        continue

    print(numero, end=" ")

