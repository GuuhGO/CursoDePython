import matplotlib.pyplot as plt
lista_eixo_x = [8,10,12,14,16]
lista_eixo_y = [1,9,4,15,12]
plt.plot(lista_eixo_x, lista_eixo_y)
plt.title("Vendas no dia 12/01/2022")
plt.ylabel("Número de Vendas")
plt.xlabel("Horário")
plt.grid(True)
plt.show()