class Canino:
    def __init__(self,peso,altura,idade,raca):
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.raca = raca
    def Correr(self):
        print("Correndo...")
    def Atacar(self):
        print("Atacando...")
    def Comer(self):
        print("Comendo...")
    def Latir(self):
        print("Latindo...")
bandit = Canino(16.0,50,5,"Pitbull")
for n,att in enumerate(dir(bandit),1):
    print(f"{n}: {att}")
bandit.Correr()
bandit.Atacar()
bandit.Comer()
bandit.Latir()