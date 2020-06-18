numero_maior = lambda x: x * 2

print((lambda x: x * 3)(15))

print(numero_maior(5))




imprime_func = lambda x: print(f"o numero é {x}")

seq = [1,2,3,4,5]

mapa = map(imprime_func,seq)
print(type(mapa))


print(next(mapa))
next(mapa)
print("----------")

print(list(mapa))