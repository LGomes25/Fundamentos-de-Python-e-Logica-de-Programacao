nome = 'Leonardo'
idade = 45
saldo = 45.36598
profissao = "Desenvolvedor"
linguagem = "Python"

dados = {"name": "Leonardo", "age": 45}

print()
print("Nome: %s , Idade: %d" %(nome, idade))
print()
print("Nome: {} , Idade: {}".format(nome, idade))
print()
print("Nome: {1} , Idade: {0}".format(idade, nome))
print()
print("Nome: {1} , Idade: {0}, Nome: {1}, Nome: {1}, Nome: {1}".format(idade, nome))
print()
print("Nome: {name} , Idade: {age}".format(age=idade, name=nome))
print()
print("Nome: {name} , Idade: {age}".format(**dados))
print()
print(f'Nome: {nome} , Idade: {idade}')
print()
print(f'Nome: {nome} , Idade: {idade}, Saldo:{saldo}')
print(f'Nome: {nome} , Idade: {idade}, Saldo:{saldo:.2f}')
print(f'Nome: {nome} , Idade: {idade}, Saldo:{saldo:10.2f}')