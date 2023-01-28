#CÓDIGO DE NOTAS USANDO LISTAS
notasList = []
for i in range(10):
    entrada = float(input(f"Insira a {i+1}ª nota: "))
    if(entrada < 0 or entrada > 10):
        i -= 1
    else:
        notasList.append(entrada)
    print(notasList)
print("Maior nota: ", max(notasList))
print("Menor nota: ", min(notasList))


#CÓDIGO DE NOTAS USANDO DICIONÁRIOS
"""
notasDict = {}
for i in range(10):
    nome = str(input(f"Insira o nome do {i+1}º aluno(a): "))
    entrada = float(input(f"Insira a sua nota: "))
    if(entrada < 0 or entrada > 10):
        i -= 1
    else:
        notasDict.update({
            nome:entrada
        })
print(notasDict)
for aluno in notasDict:
    if(notasDict[aluno] == max(notasDict.values())):
        print(f"Maior nota foi do {aluno}: ", notasDict[aluno])
for aluno in notasDict:
    if(notasDict[aluno] == min(notasDict.values())):
        print(f"Menor nota foi do {aluno}: ",notasDict[aluno])
"""

"""
Nomes para testar o programa com dicionários:
Maria
Sabrina
Heitor
Pedro
Santiago
Isabella
Heloísa
Sara
Isabel
Carlos
"""