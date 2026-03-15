# setdefault - inclui nova chave/valor no dicionario, se a chave já existir, retorna quando chamado em print o valor existente no dicionário e não faz alteração

contato = {'nome': 'Leonardo', 'fone': '99999-1111'}

print(f'Dicionário:\nR: {contato}')
print(f'Dicionario - incluir chave existente (nome: Jacó):\nR1: {contato.setdefault('nome', 'Jacó')}')
print(f'Dicionário:\nR: {contato}')
print(f'Dicionario - incluir chave nova (idade: 45):\nR1: {contato.setdefault('idade', 45)}')
print(f'Dicionário:\nR: {contato}')