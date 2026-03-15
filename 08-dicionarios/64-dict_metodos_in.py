# in - verifica a existencia de chaves dentro do dicionario

contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
    'munha@mail.com': {'nome': 'Mun-Ha', 'fone': '888888-5555'},
    'guerreiro@mail.com': {'nome': 'Gato', 'fone': '99999-4444'},
    'tilah@mail.com': {'nome': 'Tilah', 'fone': '33333-4444'},
}

print(f'Verificar se no dicionario exite a chave (mandibula@mail.com):\nR: {'mandibula@mail.com' in contatos}')
print(f'Verificar se no dicionario exite a chave (boladao@mail.com):\nR: {'boladao@mail.com' in contatos}')
print(f'Verificar se valor (idade) existe na chave (mandibula@mail.com):\nR: {'idade' in contatos["mandibula@mail.com"]}')
print(f'Verificar se valor (fone) existe na chave (mandibula@mail.com):\nR: {'fone' in contatos["mandibula@mail.com"]}')