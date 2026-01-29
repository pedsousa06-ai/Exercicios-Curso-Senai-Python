def iden_par_impar(n1, n2):
    pares = 0
    impares = 0

    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares



n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

pares, impares = iden_par_impar(n1, n2)


print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
