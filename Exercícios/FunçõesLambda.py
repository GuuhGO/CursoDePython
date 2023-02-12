# lambda argumentos: expressões
r = lambda x, func: x + func(x)

print(r(2, lambda x: x*x))