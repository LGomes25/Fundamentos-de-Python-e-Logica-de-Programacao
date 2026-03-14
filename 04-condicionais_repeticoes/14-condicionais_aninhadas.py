conta_normal = False
conta_universitaria = False

print('Qual tipo de conta? \n1 - Normal; 2 - Universitária')
tipo = int(input())
if tipo == 1:
    conta_normal=True
elif tipo ==2:
    conta_universitaria=True
else:
    print('Não é possivel realizar movimentações, informe uma conta válida!')

saldo = 2000
cheque_especial = 450

if conta_normal or conta_universitaria:
    saque = int(input(f'Seu saldo é de {saldo}, quanto deseja sacar? '))

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial"')
    else:
        print('Saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
        print('Saldo insuficiente!')
