# get - retorna o valor da chave pesquisada

contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
}
print(f'Dicionário:\nR: {contatos}')
print(f'Dicionario - apresentar o valor da chave idade (inexistente):\nR: {contatos.get('idade')}')
print(f'Dicionario - apresentar o valor da chave idade (inexistente):\nR: {contatos.get('idade',{})}')
print(f'Dicionario - apresentar o valor da chave mandibula@mail.com:\nR: {contatos.get('mandibula@mail.com')}')
print(f'Dicionario - apresentar o valor da chave mandibula@mail.com:\nR: {contatos.get('mandibula@mail.com',{})}')