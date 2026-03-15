# del - exclui chave/valor e sub-chaves/valor dentro dos dicionarios

contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
    'munha@mail.com': {'nome': 'Mun-Ha', 'fone': '888888-5555'},
}
print(f'Dicionario: {contatos}')
del contatos['mandibula@mail.com']
print(f'Exclusão da chave (mandibula@mail.com):\nR: {contatos}')
del contatos['munha@mail.com']['fone']
print(f'Exclusão da sub-chave (fone) da chave (munha@mail.com):\nR: {contatos}')