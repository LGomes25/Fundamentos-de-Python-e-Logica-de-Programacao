
# copy - cria uma nova lista baseada na original, alterações não são refletidas
lista = [1, "python", [40, 30, 20]]
listacopiada = lista
lista2 = lista.copy()

print(f'Id da Lista original: {id(lista)}')
print(f'Id da Lista copiada diretamente : {id(listacopiada)}')
print(f'Id da Lista2 copia: {id(lista2)}')

listacopiada[0] = 4

print('\nCom o uso do copy, a nova lista se disvincula da original')

print(f'Lista Original: {lista}')
print(f'Lista Copiada: {listacopiada}')
print(f'Lista2 uso do copy: {lista2}')
