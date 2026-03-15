# popitem - remove chave e valor em sequencia reversa, apresentando o par chave/valor removido se requisitado com print

contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
    'munha@mail.com': {'nome': 'Mun-Ha', 'fone': '888888-5555'},
    'guerreiro@mail.com': {'nome': 'Gato', 'fone': '99999-4444'},
    'tilah@mail.com': {'nome': 'Tilah', 'fone': '33333-4444'},
}

print(f'Dicionário:\nR: {contatos}')
print(f'Dicionario - remover chave em sequencia:\nR1: {contatos.popitem()}')
print(f'Dicionário:\nR: {contatos}')
print(f'Dicionario - remover chave em sequencia:\nR2: {contatos.popitem()}')
print(f'Dicionário:\nR: {contatos}')
print(f'Dicionario - remover chave em sequencia:\nR3: {contatos.popitem()}')
print(f'Dicionário:\nR: {contatos}')
