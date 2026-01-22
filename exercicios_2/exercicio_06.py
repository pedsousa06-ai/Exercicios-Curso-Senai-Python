n1 = float(input(" Digite o primeiro numero:"))
n2 = float(input(" Digite o segundo numero: "))
n3 = float(input(" Digite o terceiro numero: "))

if n1 > n2 > n3:
    print(f" O numero maior é {n1}")

elif n2 > n1 > n3:
    print(f" O numero maior é {n2}")

else:
    print(f" O numero maior é {n3}")