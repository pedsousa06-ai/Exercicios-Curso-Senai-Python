media = 0
soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma = soma + numero

media = soma / 5

print(f"A soma é {soma} e a média dos números é {media}")
