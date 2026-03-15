
# copy - cria um novo dicionario baseado no original, alterações não são refletidas
contatos = {
    'mandibula@mail.com': {'nome': 'Mandibula', 'fone': '77777-6666'},
}


contatos_copiado = contatos
contatos2 = contatos.copy()

print(f'Id da Contato original: {id(contatos)}')
print(f'Id da Contato copiada diretamente : {id(contatos_copiado)}')
print(f'Id da Contato2 copia: {id(contatos2)}')

contatos_copiado['mandibula@mail.com'] = {'nome': 'Josicler'}

print('\nCom o uso do copy, a nova contato se disvincula da original')

print(f'Contato Original: {contatos}')
print(f'Contato Copiada: {contatos_copiado}')
print(f'Contato2 uso do copy: {contatos2}')