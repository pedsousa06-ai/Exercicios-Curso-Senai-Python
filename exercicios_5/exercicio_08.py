def somar_positivos():
    soma = 0
    numero = int(input("Digite um número / 0 para sair: "))

    while numero != 0:
        soma += numero
        numero = int(input("Digite um número / 0 para sair: "))

    print(f"A soma dos números é: {soma}")


somar_positivos()


    