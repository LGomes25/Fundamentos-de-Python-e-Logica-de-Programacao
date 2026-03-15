lista = []

# append - adicionar itens a lista
print(f'Lista vazia: {lista[:]}')
lista.append(1)
print(f'Lista inclusão de objeto tipo numero inteiro (1): {lista[:]}')
lista.append("Python")
print(f'Lista inclusão de objeto tipo string ("Python"): {lista[:]}')
lista.append([40, 30, 20])
print(f'Lista inclusão de objeto tipo lista ([40, 30, 20]): {lista[:]}')
