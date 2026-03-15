contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
    'munha@mail.com': {'nome': 'Mun-Ha', 'fone': '888888-5555'},
    'guerreiro@mail.com': {'nome': 'Gato', 'fone': '99999-4444'},
    'tilah@mail.com': {'nome': 'Tilah', 'fone': '33333-4444'},
}

for chave in contatos:
    print(chave, contatos[chave])

print('Melhor modelo de acesso')

for chave, valor in contatos.items():
    print(f'{chave} : {valor}')