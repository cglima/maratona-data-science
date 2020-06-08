"""Programa que escolhe o mais barato dentre 5 produtos

Faça um programa que pergunte o preço de 5 produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato.

4. duas listas, uma para preço e outra para nome
"""

#pergunte o preço de 5 produtos
produtos = [
    "computador",
    "smartphone",
    "videogame",
    "cama",
    "miojo",
]

precos = [0, 0, 0, 0, 0]


for indice in range(5):
    preco_produto = float(input(f"Qual o preço do {produtos[indice]}? "))
    precos[indice] = preco_produto

print(produtos)
print(precos)

# escolha o mais barato
posicao_menor = 0
for posicao_atual in range(5):
    if (precos[posicao_atual] < precos[posicao_menor]):
        posicao_menor = posicao_atual

print(f"O produto mais barato é o {produtos[posicao_menor]} "
    + "com o preço de R${precos[posicao_menor]}")