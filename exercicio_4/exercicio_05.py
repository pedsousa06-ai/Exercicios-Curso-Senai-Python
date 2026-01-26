maior = 0

for i in range(5):
    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero

print(f"O maior número é: {maior}")
