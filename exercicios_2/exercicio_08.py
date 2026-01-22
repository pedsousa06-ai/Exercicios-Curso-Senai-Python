n1 = float(input(" Digite o primeiro valor do produto: "))
n2 = float(input(" Digite o segundo valor do produto: "))
n3 = float(input(" digite o terceiro valor: "))

if n1 < n2 < n3 :
    menor_valor = n1

elif n2 < n3 < n3:
    menor_valor = n2 

else:
    menor_valor = n3

print(f" O Valor do menor produto é {menor_valor}")
