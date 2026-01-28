n1 = int(input("Digite o número da tabuada: "))

def tabu(n1):
    for i in range(1, 11):
        print(f"{n1} x {i} = {n1 * i}")

tabu(n1)

