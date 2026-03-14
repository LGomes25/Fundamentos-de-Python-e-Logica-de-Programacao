saldo = 500
def sacar(saldo):
    saque = int(input(f'Seu saldo é de {saldo}. Informe o valor a sacar'))
    if saldo >= saque:
        saldo -= saque
        print(f'Valor de {saque} sacado!')
        print('Retire-o na gaveta.')
    else:
        print('Saldo insuficiente!')
    return saldo

def depositar(saldo, deposito):
    saldo += deposito
    print(f'Com o depósito de {deposito}, seu saldo atual agora é de {saldo}')
    return saldo

saldo = sacar(saldo)
deposito = int(input('Informe o valor a depositar em sua conta: '))
saldo = depositar(saldo, deposito)

print('Obrigado por ser nosso Cliente, tenha um bom dia!')