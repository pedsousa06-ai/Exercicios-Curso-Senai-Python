
while True:
    n = int(input("Digite um número inteiro maior ou igual a 0: "))
    if n >= 0:
        break
    print("Erro: o número deve ser maior ou igual a 0.")

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}")


