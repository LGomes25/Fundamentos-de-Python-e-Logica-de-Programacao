# Desafio

No **Núcleo de Pesquisa e Desenvolvimento da VarejoTech**, você faz parte de uma equipe responsável por criar soluções inovadoras para o setor de varejo.  

Hoje, o desafio é **automatizar a análise de produtos** para uma nova linha de caixas inteligentes.  

Cada produto recebe:
- Uma etiqueta com seu **preço**
- Uma indicação se está em **promoção**  

Seu sistema deve receber:
- O **preço do produto**
- Um **código** que indica se ele está em promoção (`"S"` para sim, `"N"` para não)

### Regras
- Se o produto estiver em promoção, aplicar **desconto de 10%** e informar o valor final.
- Caso contrário, o preço permanece o mesmo.
- O objetivo é garantir que o caixa inteligente sempre mostre o valor correto ao cliente, evitando erros e otimizando o atendimento.

---

## Implementação

O programa deve:
1. Ler o preço do produto (um número decimal positivo) e o código de promoção (`"S"` ou `"N"`), separados por espaço em uma única linha.
2. Calcular e exibir o valor final do produto, com **duas casas decimais**, aplicando o desconto apenas se o código for `"S"`.
3. Considerar apenas entradas válidas.

---

## Entrada
Uma única linha contendo:
- O preço do produto (número decimal positivo)  
- O código de promoção (`"S"` ou `"N"`)  

Separados por espaço.

---

## Saída
Uma única linha contendo o **valor final do produto**, com duas casas decimais.

---

## Exemplos

| Entrada   | Saída  |
|-----------|--------|
| 100.00 S  | 90.00  |
| 59.90 N   | 59.90  |
| 200.50 S  | 180.45 |
| 10.00 N   | 10.00  |