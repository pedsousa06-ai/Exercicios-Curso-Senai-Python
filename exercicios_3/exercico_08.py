valor = int(input("Digite o valor do resgate em Rs: "))

notas_100 = valor // 100
sobra = valor % 100

notas_50 = sobra // 50
sobra = sobra % 50

notas_20 = sobra // 20
sobra = sobra % 20

notas_10 = sobra // 10
sobra = sobra % 10

notas_5 = sobra // 5
sobra = sobra % 5

notas_2 = sobra // 2
sobra = sobra % 2

notas_1 = sobra // 1
sobra = sobra % 1

print(f" Voce Recebera: {notas_100} Notas de 100 ")
print(f"  Voce Recebera: {notas_100} Notas de 50 ")
print(f"  Voce Recebera: {notas_20} Notas de 20 ")
print(f"  Voce Recebera: {notas_10} Notas de 10  ") 
print(f"  Voce Recebera: {notas_5} Notas de 5 ")
print(f"  Voce Recebera: {notas_2} Notas de 2 ")
print(f"  Voce Recebera: {notas_1} Notas de 1 ")
print(f" A sua Sobra é: {sobra} ")