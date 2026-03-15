pessoa = {'nome': 'Leonardo', 'idade':45, 'telefone':'99999-1111'}

print(f'\nDict - listar tudo: {pessoa}')
print(f'\nDict - Acesso direto por chave(nome): {pessoa['nome']}')
print(f'\nDict - Acesso direto por chave(idade): {pessoa['idade']}')
print(f'\nDict - Acesso direto por chave(telefone): {pessoa['telefone']}')

# Modificando os dados do dicionário
pessoa['nome'] = "Michelle"
pessoa['idade'] = 46
pessoa['telefone'] = '33333-6666'

print(f'\nDict - listar tudo com modificação: {pessoa}')