# Inicialização das vairiaveis
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Modulo direto, porem confuso caso comparações sequenciais muito longas
print(f'Saldo: {saldo}, Limite: {limite}, Conta Especial: {conta_especial}, Saque: {saque}')
exp = (saldo >= saque and saque <= limite) or (saldo >= saque and conta_especial)
print('Consigo realizar o saque?', exp)

# Módulo dividido de comparações por etapas e armazenamentos modulares
print(f'Saldo: {saldo}, Limite: {limite}, Conta Especial: {conta_especial}, Saque: {saque}')
conta_normal_com_saldo = saldo >= saque and saque <= limite
conta_especial_com_saldo = saldo >= saque and conta_especial
saque_autorizado = conta_normal_com_saldo or conta_especial_com_saldo
print('Consigo realizar o saque?', saque_autorizado)