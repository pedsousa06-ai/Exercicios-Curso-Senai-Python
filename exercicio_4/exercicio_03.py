nome = input( " digite o seu nome: ")

while len(nome) <3:
    nome = input( "Digite o seu nome: " )


idade = int(input(" Digite a sua idade "))

while idade < 0 or idade > 150:
    print("  erro  ")
    idade = input(" Digite a sua idade: ")


salario = float(input(" Digite o valor do seu salario: "))

while salario < 1:
    print(" erro ")
    salario = float(input(" Digite o valor do seu salario: "))


sexo = input(" Digite seu sexo:\n F para feminino | M para masculino: ")


while sexo != "F" and sexo != "M":
    print(" sexo invalido ")
    sexo = input(" Digite seu sexo:\n F para feminino | M para masculino: ")

estado_civil = input(" Digite seu estado civil:\n  S Para solteiro | C para Casado | V Para viuvo | D Para divorciado :")

while estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    print(" Erro ")
    estado_civil = input(" Digite seu estado civil:\n  S Para solteiro | C para Casado | V Para viuvo | D Para divorciado :")

print("------------------------------------------")
print(f" O seu nome é:  {nome}")
print(f" A sua idade é de:  {idade}")
print(f" O seu salario é de:  {salario}")
print(f" O Seu sexo é:  {sexo}")
print(f" O seu estado civil é de {estado_civil}")
print("------------------------------------------")
print(" Programa finalizado ")
print("------------------------------------------")