# Informando: inicio(start), fim(stop) e passo(step) => [start: stop [, step]]

tupla = tuple("parelelepipedo")

print(f'\nTupla - acesso fatiamento: {tupla}')
print(f'Primeiro objeto: {tupla[0]}')
print(f'Ultimo objeto: {tupla[-1]}')
print(f'Penultimo objeto: {tupla[-2]}')
print(f'Primeiros 3 objeto: {tupla[:3]}')
print(f'Ignorando os 3 primeiros objeto: {tupla[3:]}')
print(f'Um pedaço com objetos da tupla: {tupla[3:8]}')
print(f'Um pedaço com objetos da tupla com steps (2): {tupla[3:8:2]}')
print(f'Todos os caracteres independente do tamanho: {tupla[:]}')
print(f'Espelhamento da tupla: {tupla[::-1]}')