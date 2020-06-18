while True:
    try:
        nota = float (input("Digite uma nota de 0 a 100: "))

        if(nota > 0 and nota < 100):
            print("O numero digitado é válido")
            break
        else:
            raise ValueError ("O numero digitado é inválido. ")
    except ValueError as error:
        print(error)

print("fim do programa")