nome = input(" Digite o nome do aluno ")
n1 = float(input(" Digite a primeira nota: "))
n2 = float(input(" Digite a segunda nota: "))

media = (n1 + n2) /2

if media == 10:
    print(f" o Aluno {nome} foi Aprovado com Distinção ")

elif media >= 7:
    print(f" O aluno {nome} foi Aprovado ")

elif media < 7:
    print(f" O aluno {nome} foi reprovado ")    