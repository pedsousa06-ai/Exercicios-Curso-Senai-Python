def validador():
    senha = input("Digite a senha: ")

    if len(senha) >= 8:
        print("Senha válida")
        return True
    else:
        print("Senha inválida (mínimo 9 caracteres)")
        return False    
validador()
                        
