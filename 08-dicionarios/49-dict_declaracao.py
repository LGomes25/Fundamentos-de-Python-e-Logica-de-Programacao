# Dicionarios: contem par chave e valor delimitado por chaves ex: {'chave': 'valor'}

pessoa = {'nome': 'Leonardo', 'idade':45}
print(f'Dicionario - criacao direta: {pessoa}')

pessoa2 = dict(nome="Michelle", idade=46)
print(f'Dicionario - criacao por construtor: {pessoa2}')

pessoa['telefone'] = '99999-1111'
print(f'Dicionario - inclusão de novo par chave/valor: {pessoa}')