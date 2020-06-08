"""Programa que escolhe o mais barato dentre 5 produtos

Faça um programa que pergunte o preço de 5 produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato.

3. Uma lista bidimensional com preço e nome
"""

#pergunte o preço de 5 produtos
produtos = [
    ["computador", 0 ],
    ["smartphone", 0 ],
    ["videogame", 0 ],
    ["cama", 0 ],
    ["miojo", 0],
]

for indice in range(5):
    preco_produto = float(input(f"Qual o preço do {produtos[indice][0]}? "))
    produtos[indice][1] = preco_produto

print(produtos)

# escolha o mais barato
posicao_menor = 0
for posicao_atual in range(5):
    if (produtos[posicao_atual][1] < produtos[posicao_menor][1]):
        posicao_menor = posicao_atual

print(f"O produto mais barato é o {produtos[posicao_menor][0]} com o preço de R${produtos[posicao_menor][1]}")