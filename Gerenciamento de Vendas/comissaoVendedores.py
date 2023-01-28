comissao = 0.05
vendedores = {
    "Vendedor01":{
        "Nome":"João",
        "Idade": 35,
        "Email": "joao@joao",
        "Senha": "joao123",
        "Total de Produtos Vendidos": 40,
        "Valor total de vendas": 40000.00
    },
    "Vendedor02":{
        "Nome":"Felipe",
        "Idade": 27,
        "Email": "felipe@felipe",
        "Senha": "felipe123",
        "Total de Produtos Vendidos": 50,
        "Valor total de vendas": 50000.00
    },
    "Vendedor03":{
        "Nome":"Danilo",
        "Idade": 25,
        "Email": "danilo@danilo",
        "Senha": "danilo123",
        "Total de Produtos Vendidos": 75,
        "Valor total de vendas": 75000.00
    }
}
email = ""
senha = ""
print('Verifique a sua comissão deste mês!')
print('TELA DE LOGIN:')
while email == "":
    emailExiste = False
    email = input("Email: ")
    for vendedor in vendedores:
        if(email == vendedores[vendedor]["Email"]):
            emailExiste = True
            break
    if(emailExiste == False):
        print("Usuário não encontrado!")
        email = ""
    else:
        while senha == "":
            senhaCorreta = False
            senha = input("Senha: ")
            for vendedor in vendedores:
                if(senha == vendedores[vendedor]["Senha"]):
                    senhaCorreta = True
                    break
            if(senhaCorreta == False):
                print("Senha Incorreta")
                senha = ""
            else:
                print("\n")
                for chaves in vendedores[vendedor]:
                    if(chaves != "Email" and chaves != "Senha"):
                        if(chaves == "Valor total de vendas"):
                            print(f"{chaves}: R$%.2f" % vendedores[vendedor][chaves])
                        else:
                            print(f"{chaves}: {vendedores[vendedor][chaves]}")
                comissaoVendedor = vendedores[vendedor]["Valor total de vendas"]*comissao
                print(f"\nSua comissão: R$%.2f" % comissaoVendedor)
                        