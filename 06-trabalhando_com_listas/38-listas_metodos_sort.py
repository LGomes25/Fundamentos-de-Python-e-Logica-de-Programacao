# sort - ordenação da lista

linguagens = ['python', 'js', 'c','java', 'csharp']
print(linguagens)
linguagens.sort()
print(f'Ordenação alfabética crescente: {linguagens}')

print()

linguagens = ['python', 'js', 'c','java', 'csharp']
print(linguagens)
linguagens.sort(reverse=True)
print(f'Ordenação alfabética inversa: {linguagens}')

print()

linguagens = ['python', 'js', 'c','java', 'csharp']
print(linguagens)
linguagens.sort(key=lambda x: len(x))
print(f'Ordenação ordem de tamanho do objeto: {linguagens}')

print()

linguagens = ['python', 'js', 'c','java', 'csharp']
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(f'Ordenação ordem inversa de tamanho do objeto: {linguagens}')