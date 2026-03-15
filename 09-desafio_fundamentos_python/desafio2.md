# Desafio

No **Núcleo de Pesquisa e Desenvolvimento da empresa VarejoFuturo**, você faz parte de uma equipe responsável por analisar tendências de produtos para o setor varejista.  

Seu time recebe diariamente listas de produtos sugeridos por diferentes especialistas e precisa identificar rapidamente quais produtos são mais populares para priorizar o desenvolvimento de novos serviços.  

Para isso, você deve criar um programa que receba uma lista de nomes de produtos (separados por espaço) e retorne o nome do produto mais frequente.  
Caso haja empate, retorne o produto que aparece primeiro na lista original.  

Sua solução será fundamental para acelerar as decisões do núcleo e garantir que os produtos certos cheguem ao mercado!

---

## Implementação

O programa deve:
1. Ler uma linha contendo nomes de produtos separados por espaço.  
2. Identificar qual produto aparece mais vezes na lista.  
3. Em caso de empate, retornar o que aparece primeiro na lista.  
4. Utilizar apenas estruturas básicas como **listas** e **tuplas** para resolver o problema.

---

## Entrada
- Uma única linha contendo nomes de produtos separados por espaço.  
- Cada nome é uma **string** sem espaços internos.

---

## Saída
- Uma única **string** representando o nome do produto mais frequente na lista.  
- Em caso de empate, retornar o que aparece primeiro.

---

## Exemplos

| Entrada                         | Saída   |
|---------------------------------|---------|
| `cafe leite pao leite pao pao`  | `pao`   |
| `arroz feijao arroz feijao`     | `arroz` |
| `banana maca pera`              | `banana`|
| `suco suco agua agua agua`      | `agua`  |