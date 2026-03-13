# São operadores utilizados para verificar se um objeto está presente em uma sequência 

frutas = ['limão', 'uva', 'laranja']

print(f'\nLista de frutas:{frutas}\n')
print('Tenho laranja na minha lista?', 'laranja' in frutas)
# Case sensitive
print('Tenho Laranja na minha lista?', 'Laranja' in frutas)
print('NÂO Tenho limão na minha lista?', 'limão' not in frutas)
print('\n')


curso = "Curso de python"

print('Tenho python em "curso"?', 'python' in curso)
# Case sensitive
print('Tenho Python em "curso"?', 'Python' in curso)