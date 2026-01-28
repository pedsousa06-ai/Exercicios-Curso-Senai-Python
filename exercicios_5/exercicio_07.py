def validador():
    senha = input("Digite a senha: ")

    if len(senha) > 8:
        print("Senha válida")
    else:
        print("Senha inválida (mínimo 9 caracteres)")

        return senha 
    
validador()