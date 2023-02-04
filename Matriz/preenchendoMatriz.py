matriz = [[0,0,0],[0,0,0]]
print(f"{'Preenchendo a Matriz':-^50}")
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        matriz[lin][col] = int(input("Digite um número: "))
print(f"{'Imprimindo a Matriz':-^50}")
print(f"{'':-^50}")
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz[lin][col], end='\t')
    print('|')
    print(f"{'':-^50}")
