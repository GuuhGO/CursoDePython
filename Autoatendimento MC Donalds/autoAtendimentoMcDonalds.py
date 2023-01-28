menu = {
    "lanches":{
        1 : "Big Mac",
        2 : "Big Tasty",
        3 : "Cheeseburger",
        4 : "MC Chicken"
    },
    "acompanhamentos":{
        1 : "Batata Pequena",
        2 : "Batata Média",
        3 : "Batata Grande"
    },
    "bebidas":{
        1 : "Refrigerante",
        2 : "Suco",
        3 : "Água"
    }
}
pedido = {
    "lanches":{
        "Lanche": "",
        "Quantidade": 0
    },
    "acompanhamentos":{
        "Acompanhamento": "",
        "Quantidade": 0
    },
    "bebidas":{
        "Bebida": "",
        "Quantidade": 0
    }
}
print("Bem-Vindo ao MC Donald's".upper())
print("Estas são nossas opções de lanche:")
for i in range(len(menu["lanches"])):
    print(
        f"{i+1} -",menu["lanches"][i+1]
        )
print()
pedido.update({
    "lanches":{
        "Lanche": menu["lanches"][int(input("Insira o número do que você deseja: "))],
        "Quantidade": int(input("Insira a quantidade que deseja: "))
    }
})
print("\nEstas são nossas opções de acompanhamentos:")
for i in range(len(menu["acompanhamentos"])):
    print(
        f"{i+1} -",menu["acompanhamentos"][i+1]
        )
print()
pedido.update({
    "acompanhamentos":{
        "Acompanhamento": menu["acompanhamentos"][int(input("Insira o número do que você deseja: "))],
        "Quantidade": int(input("Insira a quantidade que deseja: "))
    }
})
print("\nEstas são nossas opções de bebidas:")
for i in range(len(menu["bebidas"])):
    print(
        f"{i+1} -",menu["bebidas"][i+1]
        )
print()
pedido.update({
    "bebidas":{
        "Bebida": menu["bebidas"][int(input("Insira o número do que você deseja: "))],
        "Quantidade": int(input("Insira a quantidade que deseja: ")) 
    }
})
print()
print('Finalização do Pedido:'.upper())
for itens in pedido:
    for detalhes in pedido[itens]:
        print(
            f"{detalhes}: ", pedido[itens][detalhes]
            )
        if(pedido[itens][detalhes] == "Quantidade"):
            print()