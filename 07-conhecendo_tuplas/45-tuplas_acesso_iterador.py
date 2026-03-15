veiculos = ("gol", "celta", "palio",)

for carro in veiculos:
    print(carro)

print('Tuplas com enumerador')

for indice, caror in enumerate(veiculos):
    print(f'{indice} : {carro}')