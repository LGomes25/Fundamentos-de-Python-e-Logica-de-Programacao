# Informando: inicio(start), fim(stop) e passo(step) => [start: stop [, step]]

lista = list("parelelepipedo")

print(f'\nLista - acesso fatiamento: {lista}')
print(f'Primeiro objeto: {lista[0]}')
print(f'Ultimo objeto: {lista[-1]}')
print(f'Penultimo objeto: {lista[-2]}')
print(f'Primeiros 3 objeto: {lista[:3]}')
print(f'Ignorando os 3 primeiros objeto: {lista[3:]}')
print(f'Um pedaço com objetos da lista: {lista[3:8]}')
print(f'Um pedaço com objetos da lista com steps (2): {lista[3:8:2]}')
print(f'Todos os caracteres independente do tamanho: {lista[:]}')
print(f'Espelhamento da lista: {lista[::-1]}')