# Este código faz a correção de uma entrada com números decimais separadas por vírgula e transforma em '.'.
# Por exemplo: inserir um valor 12,5 irá retornar 12.5

def correct(val):
    if(',' in val):
        lista = list(val)
        lista[lista.index(',')] = '.'
        val = "".join(lista)
        val = float(val)
        return val
    else:
        val = float(val)
        return val