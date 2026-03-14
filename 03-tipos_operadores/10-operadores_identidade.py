# Operado "is" e "is not" comparam posição de memória retornando um boolean

saldo = 1000
limite = 500

print(f'Saldo={saldo}, Limite={limite}')
print('Saldo ocupa a mesma posição de memória de limite?', saldo is limite)
print('Saldo não ocupa a mesma posição de memória de limite?', saldo is not limite)
