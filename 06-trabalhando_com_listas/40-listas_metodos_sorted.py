# sorted - ordenação da lista, mesmas características do sort

linguagens = ['python', 'js', 'c','java', 'csharp']
print(linguagens)
print(f'Ordenação alfabética crescente alfabética: {sorted(linguagens)}')
print(f'Ordenação alfabética decrescente alfabética: {sorted(linguagens, reverse=True)}')
print(f'Ordenação crescente tamanho de objeto: {sorted(linguagens, key=lambda x: len(x))}')
print(f'Ordenação decrescente tamanho de objeto: {sorted(linguagens, key=lambda x: len(x), reverse=True)}')