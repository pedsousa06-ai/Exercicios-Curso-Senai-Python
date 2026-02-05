#LISTAS E CONSTANTES

#As constantes são valores que não se mudam o valor dela e se pode alterar 
#ela a partir de seu valor e podemos adionar ela
#incluindo uma letra maiuscula para definir ela.

# As listas são Listas em Python são estruturas de dados versáteis e ordenadas, definidas por colchetes [], 
# #que funcionam como contêineres para armazenar coleções de itens, incluindo tipos mistos (strings, números, booleans). 
# #Elas são mutáveis (podem ser alteradas após a criação), suportam duplicatas e utilizam índices baseados em zero para acessar elementos. 
lista_nomes =[]

opcao = -1
while opcao != "0":
    opcao = input("Digite o nome da pessoa que deseja adicionar [0] - Sair :   ")
    if opcao != "0":
        lista_nomes.append(opcao)

print("A sua lista de nomes é:",lista_nomes)