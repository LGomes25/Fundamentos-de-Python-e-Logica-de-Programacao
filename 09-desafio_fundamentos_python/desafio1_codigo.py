entrada = input('Informe o preço do produto e o código da promoção separados por um espaço:\n= ').strip()
preco_str, codigo_promocao = entrada.split()

preco = float(preco_str)
codigo_promocao = codigo_promocao.upper()
mensagem = ""

if codigo_promocao == 'S':
    preco_final = preco * 0.9
    mensagem = "Desconto aplicado de 10% ao valor inicial do produto"
else:
    preco_final = preco
    mensagem = "Produto fora da promoção"

print(f"Valor a pagar: {preco_final:.2f} - {mensagem}")