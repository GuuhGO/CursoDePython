import locale

def convert(val):
    if(',' in val):
        lista = list(val)
        lista[lista.index(',')] = '.'
        val = "".join(lista)
        val = float(val)
        return val
    else:
        val = float(val)
        return val

numero = 0.0
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
numero = input("Insira o numero: ")
numero = convert(numero)
print(numero, type(numero))
numero = locale.currency(numero, grouping=True, symbol=True)
print(numero)