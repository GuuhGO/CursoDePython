cadeiras = [
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"],
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"],
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"],
    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]
]
def imprimeCadeiras():
    for lin in range(len(cadeiras)):
        print(f"{'':-^{espacador}}")
        for col in range(len(cadeiras[lin])):
            print('| ', end='')
            print(cadeiras[lin][col], end=' ')
            if(col == 7):
                print('| ', end='\n')
    print(f"{'':-^{espacador}}")

def verificarEmCadeiras(valor):
    consta = False
    for lin in range(len(cadeiras)):
            if(valor in cadeiras[lin]):
                encontra = cadeiras[lin].index(valor)
                cadeiras[lin][encontra] = "  "
                # imprimeCadeiras()
                consta = True
                return consta
    return consta        
espacador = 41
print(F"{'BEM VINDO AO CINEMA':^{espacador}}")
while True:
    print("Essas são as cadeiras disponíveis\nEscolha uma para reservar:")
    imprimeCadeiras()
    escolha = input("Insira a cadeira que deseja ou digite 'q' para sair.\nR: ").upper()
    if(escolha != 'Q'):
        if(verificarEmCadeiras(escolha)):
            print("\nCadeira reservada com sucesso\n".upper())
        else:
            print("\n\nDesculpe, esta cadeira não está disponível ou sua resposta é inválida.")
            input("\nAperte Enter para continuar...")
    else:
        print("Saindo...")
        break