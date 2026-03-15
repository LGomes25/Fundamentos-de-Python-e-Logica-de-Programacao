matriz = [
    [1, 'a', 2],
    ["b", 3, 4],
    [6, 5, 'c']
]

print(f'\nLista - lista aninhada: {matriz}')
print(f'\nLista - Acesso direto por indice [0] (linha 1): {matriz[0]}')
print(f'Lista - Acesso direto por indice [1] (linha 2): {matriz[1]}')
print(f'Lista - Acesso direto por indice [2] (linha 3): {matriz[2]}')
print(f'\nLista - Acesso direto por indice [0][0] (linha 1 / col 1): {matriz[0][0]}')
print(f'Lista - Acesso direto por indice [0][-1] (linha 1 / col 3): {matriz[0][-1]}')
print(f'Lista - Acesso direto por indice [-1][-1] (linha 3 / col 3): {matriz[-1][-1]}')
print(f'Lista - Acesso direto por indice [2][2] (linha 3 / col 3): {matriz[2][2]}')