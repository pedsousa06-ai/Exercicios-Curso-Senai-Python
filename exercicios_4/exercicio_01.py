nota = int(input("Digite o valor da sua nota entre zero e dez: "))

while nota < 0 or nota > 10:
    print("Nota incorreta")
    nota = int(input("Digite o valor da sua nota entre zero e dez: "))

print("Nota correta")
