nome = "LeoNardO"

print('\nTodas letras em maiusculas: ')
print(nome.upper())
print('\nTodas letras em minusculas: ')
print(nome.lower())
print('\nPrimeira letra maiuscula e restante das letras em minusculas: ')
print(nome.title())

texto = "   Olá mundo!!    "

print(f'\nTexto a corrigir: {texto}.')
print('\nRetirada de espeços em ambos os lados')
print(texto.strip()+"!")
print('\nRetirada de espeços somete a esquerda')
print(texto.lstrip()+"!")
print('\nRetirada de espeços somete a direita')
print(texto.rstrip()+"!")

menu = "Python"

print('\nMontar um menu do tipo:')
print('----' + menu + '----')
print('\nUtilizando um centralizador:')
print(menu.center(14,"-"))

print('\nMontar um menu do tipo:')
print('P-y-t-h-o-n')
print('\nUtilizando um join:')
print("-".join(menu))
