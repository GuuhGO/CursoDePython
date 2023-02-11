usuarios = {
    "Usuarios": {
        
    },
}

print("BEM VINDO!!")

def adicionaUsuario():
    print("Cadastro de usuário!")
    userName = input("Insira o nome de usuário: ")
    usuarios.update({"Usuarios" : {userName: ""}})
    password = input("Insira a senha: ")
    usuarios.update({"Usuarios":{userName:{"Senha":password}}})
    print(usuarios)
def login():
    while True:
        loginUserName = input("Usuário: ")
        if(loginUserName in usuarios["Usuarios"]):
            while True:
                loginPassword = input("Senha: ")
                if(loginPassword == usuarios["Usuarios"][loginUserName]["Senha"]):
                    print("Login efetuado com sucesso!\nAguarde, estamos carregando as informações...")
                    break
                else:
                    print("Senha incorreta, tente novamente!")
            break
        else:
            print("Usuário não encontrado!\nTente novamente")
def menu():
    while True:
        print(
            "Selecione o que deseja fazer:",
            "\n1 - Cadastrar usuário",
            "\n2 - Logar",
            "\n3 - Mostrar usuários",
            "\n4 - Sair"
            )
        escolha = int(input("Resposta: "))
        match escolha:
            case 1:
                adicionaUsuario()
                print("Usuario adicionado!\n")
            case 2:
                login()
            case 3:
                print(usuarios)
            case 4:
                print("Saindo...")
                exit()
            case _:
                print("Opção inválida!")
menu()