""" Programa que escolhe o mais barato dentre 5 produtos

Faça um programa que pergunte o preço de 5 produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato.

2. uma lista unidimensional com preço e nome
"""

#pergunte o preço de 5 produtos
produtos = [
    "computador", 0 ,
    "smartphone", 0 ,
    "videogame", 0 ,
    "cama", 0 ,
    "miojo", 0]

for i in range(1,10,2):
    preco_produto = float(input(f"Qual o preço do {produtos[i-1]}? "))
    produtos[i] = preco_produto

print(produtos)

# escolha o mais barato
posicao_menor = 1
for posicao_atual in range(1,10,2):
    if (produtos[posicao_atual] < produtos[posicao_menor]):
        posicao_menor = posicao_atual

print(f"O produto mais barato é o {produtos[posicao_menor-1]} com o preço de R${produtos[posicao_menor]}")



# imprimir o produto que o usuário vai comprar