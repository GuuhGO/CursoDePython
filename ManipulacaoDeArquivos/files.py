import re

ENC = "UTF-8"
ARQUIVO_PRODUTOS = r"ManipulacaoDeArquivos\Pessoas.txt"
try:
    with open(ARQUIVO_PRODUTOS, "x", encoding=ENC) as file:
        print(file.write("id,produto,preco\n"))
except FileExistsError:
    with open(ARQUIVO_PRODUTOS, "r+", encoding=ENC) as file:
        if file.read() == "":
            file.write("id,produto,preco\n")


class Pessoas:
    def __init__(self):
        self.nome = 0
        self.idade = 0
        self.peso = 0

    def cadastraPessoa(self, nome: str, idade: int, peso: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        with open(ARQUIVO_PRODUTOS, "r+", encoding=ENC) as file:
            larg = len(file.readlines())
            verif = False
            file.seek(0)
            for count in file.readlines():
                if f"{nome},{idade},{peso}" in count:
                    verif = True
                    print("Dados já cadastrados: ", file.readline())
                    break
            if verif == False:
                file.seek(0)
                if "\n" not in file.readlines()[larg - 1]:
                    file.write(f"\n{larg},{nome},{idade},{peso}\n")
                else:
                    file.write(f"{larg},{nome},{idade},{peso}\n")

    def consultaPessoa(self, id=-1, nome="NoneValue", idade=-1, peso=-1.0):
        self.id = str(id)
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        matches = 0
        with open(ARQUIVO_PRODUTOS, "r+", encoding=ENC) as file:
            dados = []
            for count in file.readlines():
                dados.append(count.strip("\n").split(","))
            for count in dados[1:]:
                file.seek(0)
                if (
                    re.search(rf"{self.id}", str(count[0])) != None
                    or re.search(rf"{self.nome.casefold()}", str(count[1])) != None
                    or re.search(rf"{self.nome.capitalize()}", str(count[1])) != None
                    or re.search(rf"{self.nome}", str(count[1])) != None
                    or re.search(rf"{self.idade}", str(count[2])) != None
                    or re.search(rf"{self.peso}", str(count[3])) != None
                ):
                    print(count)
                    matches += 1
            print(f"\n{matches} correspondências encontradas!\n")


obj1 = Pessoas()
obj1.consultaPessoa(nome="c")

# 0 - ID
# 1 - Nome
# 2 - Idade
# 3 = peso
