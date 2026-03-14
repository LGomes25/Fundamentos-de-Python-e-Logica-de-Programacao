# Fatiação: retornar dub-strings
# Informando: inicio(start), fim(stop) e passo(step) => [start: stop [, step]]

nome = "Leonardo Soares Gomes"

print(nome)
print(f'Primeiro caracter: {nome[0]}')
print(f'Ultimo caracter: {nome[-1]}')
print(f'Penultimo caracter: {nome[-2]}')
print(f'Primeiros 12 caracteres: {nome[:12]}')
print(f'Ignorando os 12 primeiros caracteres: {nome[12:]}')
print(f'Um pedaço da string: {nome[12:19]}')
print(f'Um pedaço da string com steps (2): {nome[12:19:2]}')
print(f'Todos os caracteres independente do tamanho: {nome[:]}')
print(f'Espelhamento da string: {nome[::-1]}')
