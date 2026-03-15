# Ao declarar uma tupla, usa-se parenteses e ao final da sequencia, coloca-se uma virgula para caracterizar a tupla

frutas = ('laranja', 'maca', 'uva',)
print(f'\nTupla - Declaração direta: {frutas}')

letras = tuple("python")
print(f'\nTupla - Declaração por contrutor: {letras}')

numeros = tuple([1, 2, 3, 4])
print(f'\nTupla - Declaração por contrutor: {numeros}')

pais = ("Brasil", "Canada", 12,)
print(f'\nTupla - Declaração direta com variação de objetos: {pais}')