#MÉTODO 01
matriz = [[0,0,0],[0,0,0]]
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        if(col == 0):
            matriz[lin][col] = input("Insira o nome: ")
        elif(col == 1):
            matriz[lin][col] = input(("Insira a idade: "))
        elif(col == 2):
            matriz[lin][col] = input("Insira o CPF: ")

print(f"{'Imprimindo a matriz':-^50}")
print(
f"""
{'':-^49}
|{'Nome':^15}|{'Idade':^15}|{'CPF':^15}|
{'':-^49}
|{matriz[0][0]:^15}|{matriz[0][1]:^15}|{matriz[0][2]:^15}|
{'':-^49}
|{matriz[1][0]:^15}|{matriz[1][1]:^15}|{matriz[1][2]:^15}|
{'':-^49}
"""
)




#MÉTODO 02
# for lin in range(len(matriz)):
#     col = 0
#     matriz[lin][col] = input("Insira o nome: ")
#     col += 1
#     matriz[lin][col] = input("Insira a idade: ")
#     col += 1
#     matriz[lin][col] = input("Insira o cpf: ")
