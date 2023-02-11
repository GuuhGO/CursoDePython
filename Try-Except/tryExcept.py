# Autor: Gustavo Guimarães de Oliveira
# Data: 11/02/2023
# Exercício usando try except para corrigir erros caso ocorram


# Tentar manipular/imprimir variável que não existe
print("Tentar imprimir variável que não existe: ")
try:
    if (True):
        print("Ola")
except NameError:
    print("A variável que você tentou imprimir não existe")
except TypeError:
    print("Você tentou tipos diferentes")
except IndentationError:
    print("Há um erro de identação")
