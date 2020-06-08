""" Programa que escolhe o mais barato dentre 5 produtos

Faça um programa que pergunte o preço de 5 produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato.

1. Resolver o programa com variaveis primitivas
"""

#pergunte o preço e o nome de 5 produtos
produto1 = "computador"
produto2 = "smartphone"
produto3 = "videogame"
produto4 = "cama"
produto5 = "miojo"

preco_produto1 = float(input(f"Qual o preço do {produto1}"))
preco_produto2 = float(input(f"Qual o preço do {produto2}"))
preco_produto3 = float(input(f"Qual o preço do {produto3}"))
preco_produto4 = float(input(f"Qual o preço do {produto4}"))
preco_produto5 = float(input(f"Qual o preço do {produto5}"))

# escolha o mais barato
# imprimir o produto que o usuário vai comprar
if(preco_produto1 <= preco_produto2
    and preco_produto1 <= preco_produto3
    and preco_produto1 <= preco_produto4
    and preco_produto1 <= preco_produto5):
    print(f"O {produto1} é o mais barato dentre os produtos. COMPRE ESTE PRODUTO, AGORA!")
elif(preco_produto2 <= preco_produto1
    and preco_produto2 <= preco_produto3
    and preco_produto2 <= preco_produto4
    and preco_produto2 <= preco_produto5):
    print(f"O {produto2} é o mais barato dentre os produtos. COMPRE ESTE PRODUTO, AGORA!")
elif(preco_produto3 <= preco_produto1
    and preco_produto3 <= preco_produto2
    and preco_produto3 <= preco_produto4
    and preco_produto3 <= preco_produto5):
    print(f"O {produto3} é o mais barato dentre os produtos. COMPRE ESTE PRODUTO, AGORA!")
elif(preco_produto4 <= preco_produto1
    and preco_produto4 <= preco_produto2
    and preco_produto4 <= preco_produto3
    and preco_produto4 <= preco_produto5):
    print(f"O {produto4} é o mais barato dentre os produtos. COMPRE ESTE PRODUTO, AGORA!")
else:
    print(f"O {produto5} é o mais barato dentre os produtos. COMPRE ESTE PRODUTO, AGORA!")