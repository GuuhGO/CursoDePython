print("Declare as variáveis do tipo lista, tupla, conjunto, matriz e dicionário e então as imprima no terminal")

varTupla = ("Banana","Maçã","Uva")
varLista = ["Carro", "Moto", "Caminhão"]
varConjunto = {"Gustavo", "Melissa", "Danilo", "Vitoria", "Felipe", "Flavia", "Rafaela", "Wallison"}
varMatrix = [['A','B','C'],
             ['D','E','F'],
             ['G','H','I']]
varDicionario = {"Nome" : "João", "Idade": 21, "Altura": 1.94}
#Impressão das variáveis sem especificações
print("Tupla (tuple): ", varTupla) #Imprime a tupla (tuple)
print("Matriz (list): ", varMatrix) #Imprime a matriz (matrix ou array multidimensional)
print("Conjunto (set): ", varConjunto) #Imprime o conjunto (set)
print("Dicionário (dict):", varDicionario) #Imprime o dicionário (dict)
print("Lista (list):", varLista) #Imprime a lista (list)
print("\n\n\n")
#Impressão das variáveis com especificações
#LISTA (list)
print("\nEspecificações da lista:")
for i in range(len(varLista)): #For que percorre os elementos da varLista, imprime o seu índice e o seu valor
    print(f"Item {i+1} [{i}]:", varLista[i])

#TUPLA (tuple)
print("\nEspecificações da Tupla:")
for i in range(len(varTupla)): #For que percorre os elementos da varTupla, imprime o seu índice e o seu valor
    print(f"Item {i+1} [{i}]:", varTupla[i])

#CONJUNTO (set)
print("\nEspecificações do Conjunto:")
countSet = 0
for elemento in varConjunto:#Laço que percorre os elementos da varConjunto (que mudam a sua ordem a cada execução), imprime o seu índice e o seu valor
    print(f"Item {countSet+1} [{countSet}]:", elemento)
    countSet += 1

#MATRIZ (list)
print("\nEspecificações da Matriz:")
for rowMatrix in range(len(varMatrix)):#Laço que percorre os elementos da varMatrix, especifica as coordenadas e imprime o seu valor
    for columnMatrix in range(len(varMatrix)):
        print(f"Linha {rowMatrix+1} e Coluna {columnMatrix+1}: ",varMatrix[rowMatrix][columnMatrix])
        if (columnMatrix == 2):
            print('\n')

#DICIONARIO (dict)
print("\nEspecificações das Propriedades do dicionário:")
print("Nome: ", varDicionario["Nome"], "\nIdade: ", varDicionario["Idade"], "\nAltura: ", varDicionario["Altura"]) #Imprime os valores das propriedades "Nome", "Idade" e "Altura" do dicionário separadamente
