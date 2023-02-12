# CRIAÇÃO DA CLASSE
class Carro:
    def __init__(self, modelo, ano, velMax, cor):
        self.modelo = modelo
        self.ano = ano
        self.velMax = velMax
        self.cor = cor
    def getModelo(self):
        return self.modelo
    def setModelo(self, modelo):
        self.modelo = modelo
    def getAno(self):
        return self.ano
    def setAno(self, ano):
        self.ano = ano
    def getVelMax(self):
        return self.velMax
    def setvelMax(self, velMax):
        self.velMax = velMax
    def getCor(self):
        return self.cor
    def setCor(self, cor):
        self.cor = cor
    def getAll(self):
        print(
            "Modelo: ", self.getModelo(),
            "\nAno: ", self.getAno(),
            "\nVelocidade Maxima: ", self.getVelMax(),
            "\nCor: ", self.getCor(),
        )

# REFERÊNCIAS DE OBJETO
Palio = Carro("Palio", 2008, 200, "Cinza")
Gol = Carro("Gol", 2005, 220, "Preto")
Celta = Carro("Celta", 2009, 190, "Vermelho")

# CHAMADA DO MÉTODO getAll()
Palio.getAll()
print()
Gol.getAll()
print()
Celta.getAll()
