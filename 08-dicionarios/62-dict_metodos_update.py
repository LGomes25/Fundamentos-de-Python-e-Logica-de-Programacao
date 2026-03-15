# update - atualiza chaves do dicionário **uidade** no exemplo abaixo observar que a chave atualizada perdeu o campo fone, pois todo o valor da chave foi substituido.

contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
}

print(f'Dicionário:\nR: {contatos}')
print(f'Dicionario - Atualizar chave (nome: Jacó):\nR1: {contatos.update({"mandibula@mail.com":{'nome', 'Jacó'}})}')
print(f'Dicionário:\nR: {contatos}')
print(f'Dicionario - incluir chave nova (tilah@mail.com):\nR2: {contatos.update({"tilah@mail.com":{'nome': 'Tilah', 'fone': '33333-4444'}})}')
print(f'Dicionário:\nR: {contatos}')