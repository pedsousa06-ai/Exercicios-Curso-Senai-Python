qtd = int(input("Quantos números você vai digitar? "))

numero = float(input("Digite um número: "))

maior = numero
menor = numero

for i in range(qtd - 1):
    numero = float(input("Digite um número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Maior número:", maior)
print("Menor número:", menor)

