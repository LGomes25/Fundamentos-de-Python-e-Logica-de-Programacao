# fromkeys: usado para criar novos dicionarios - somente com as chaves ou com valores padrão


chaves = dict.fromkeys(['nome', 'telefone'])
print(f'Dicionário - criação somente das chaves: {chaves}')

vazio = dict.fromkeys(['nome', 'telefone'], "padrão")
print(f'Dicionário - criação das chaves com valores (padrão): {vazio}')

