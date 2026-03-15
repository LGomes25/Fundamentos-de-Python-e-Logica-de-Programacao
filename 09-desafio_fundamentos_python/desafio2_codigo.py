produtos = input("Informe a sequencia de produtos:\n= ").strip().split()

mais_frequente = None
maior_contagem = -1

for produto in produtos:
    contagem = produtos.count(produto)
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto

print(f'O produto que mais se repete é: {mais_frequente}')