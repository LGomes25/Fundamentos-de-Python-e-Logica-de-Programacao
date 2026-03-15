# Aninhamento: dicionários dentro de dicionarios.
contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
    'munha@mail.com': {'nome': 'Mun-Ha', 'fone': '888888-5555'},
    'guerreiro@mail.com': {'nome': 'Gato', 'fone': '99999-4444'},
    'tilah@mail.com': {'nome': 'Tilah', 'fone': '33333-4444'},
}

print(f'Dicionario - completo: {contatos}')
print(f'Dicionario - acesso por chave unica: {contatos["guerreiro@mail.com"]}')
print(f'Dicionario - acesso por chave direcionada (telefone): {contatos["guerreiro@mail.com"]['fone']}')