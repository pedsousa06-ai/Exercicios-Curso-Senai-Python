num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

if num_1 < num_2:
    for num in range(num_1, num_2 + 1):
        print(num)
else:
    for num in range(num_1, num_2 - 1, -1):
        print(num)