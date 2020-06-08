"""Programa que escolhe o mais barato dentre 5 produtos

Faça um programa que pergunte o preço de 5 produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato.

5. um dicionário
"""

#pergunte o preço de 5 produtos
produtos = {
    'computador': 0,
    'smartphone': 0,
    'videogame': 0,
    'cama': 0,
    'miojo': 0,
}


for p in produtos:
    preco_produto = float(input(f"Qual o preço do {p}? "))
    produtos[p] = preco_produto

print(produtos)

# escolha o mais barato
posicao_menor = 'computador'
for posicao_atual in produtos:
    if (produtos[posicao_atual] < produtos[posicao_menor]):
        posicao_menor = posicao_atual

print(f"O produto mais barato é o {posicao_menor}")
print(f"O preço mais barato é o {produtos[posicao_menor]}")