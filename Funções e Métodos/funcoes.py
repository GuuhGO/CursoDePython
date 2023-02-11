usuarios = {}
print("BEM VINDO!!")
def adicionaUsuario():
    print("Cadastro de usuário!")
    userName = input("Insira o nome de usuário: ")
    usuarios.update({userName: ""})
    password = input("Insira a senha: ")
    usuarios.update({userName:{"Senha":password}})
    print(usuarios)
def login():
    while True:
        loginUserName = input("Usuário: ")
        if(loginUserName in usuarios):
            while True:
                loginPassword = input("Senha: ")
                if(loginPassword == usuarios[loginUserName]["Senha"]):
                    print("Login efetuado com sucesso!\nAguarde, estamos carregando as informações...")
                    input("Pressione ENTER para continuar")
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
        print()
        match escolha:
            case 1:
                adicionaUsuario()
                print("Usuario adicionado!\n")
            case 2:
                login()
                break
            case 3:
                print("\nUsuários cadastados:")
                for a in usuarios:
                    print(a)
                print()
            case 4:
                print("Saindo...")
                exit()
            case _:
                print("Opção inválida!\n")
menu()