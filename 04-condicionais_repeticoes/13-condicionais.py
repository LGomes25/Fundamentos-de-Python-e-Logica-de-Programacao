MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input('Informe sua idade: '))

# exemplo if / else
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH')
else:
    print('Menor de idade, não pode tirar a CNH')

# exemplo if / elif / else
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH')
elif idade>= IDADE_ESPECIAL:
    print('Menor de idade, porém com idade para fazer as aulas teóricas.')
else:
    print('Menor de idade, não pode tirar a CNH')