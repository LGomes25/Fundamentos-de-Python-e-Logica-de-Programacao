# Clear - limpa completamente o dicionário

contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
    'munha@mail.com': {'nome': 'Mun-Ha', 'fone': '888888-5555'},
    'guerreiro@mail.com': {'nome': 'Gato', 'fone': '99999-4444'},
    'tilah@mail.com': {'nome': 'Tilah', 'fone': '33333-4444'},
}

print(f'\nDicionario completo: {contatos}')
contatos.clear()
print(f'\nDicionario vazio: {contatos}')