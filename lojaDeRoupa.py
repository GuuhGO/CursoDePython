loja_de_roupa = {
    1: "Camisa social branca",
    2: "Calça Jeans azul",
    3: "Blusa de lã preta",
    4: "Vestido longo vermelho",
    5: "Tênis branco",
    6: "Bolsa de couro marrom",
    7: "Jaqueta de couro preta",
    8: "Sunglasses pretas",
    9: "Chapéu de palha",
    0: "Sapato de salto alto"
}
produtos = {
    123: "Camisa estampada",
    124: "Camisa social manga longa",
    125: "Calça jeans"
}
venda = [(123, 3, 25.55),
         (124, 2, 79.99),
         (125, 1, 99.99),]
print(f"{'NADILA MODAS E LTDA':-^46}")
item = 0
valor_total = 0
print("-" * 46)
print("C U P O M  F I S C A L".center(46, ' '))
print("ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL_UNIT(R$) ST VL")
print("-" * 46)
for indice in range(len(venda)):
    subtotal = 0
    item += 1
    produto = produtos.get(venda[indice][0])
    quantidade = venda[indice][1]
    valor = venda[indice][2]
    subtotal += quantidade * valor
    valor_total += subtotal
    print(
        f"{str(item).ljust(4)}{venda[indice][0]}{produto.rjust(37)}"
    )
    print(
        f"{str(quantidade).rjust(11)}UN X {str(valor).ljust(6)}{str(subtotal).rjust(23)}"
    )
