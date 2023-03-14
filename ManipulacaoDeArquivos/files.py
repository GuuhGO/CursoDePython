import re

ENC = "UTF-8"
ARQUIVO_PESSOAS = r"ManipulacaoDeArquivos\Pessoas.txt"
try:
    with open(ARQUIVO_PESSOAS, "x", encoding=ENC) as filePerson:
        print(filePerson.write("id,produto,preco\n"))
except FileExistsError:
    with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
        if filePerson.read() == "":
            filePerson.write("id,produto,preco\n")


class Pessoas:
    def __init__(self):
        self.nome = 0
        self.idade = 0
        self.peso = 0

    def cadastraPessoa(self, nome: str, idade: int, peso: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
            larg = len(filePerson.readlines())
            verif = False
            filePerson.seek(0)
            for count in filePerson.readlines():
                if f"{nome},{idade},{peso}" in count:
                    verif = True
                    print("Dados já cadastrados: ", filePerson.readline())
                    break
            if verif == False:
                filePerson.seek(0)
                if "\n" not in filePerson.readlines()[larg - 1]:
                    filePerson.write(f"\n{larg},{nome},{idade},{peso}\n")
                else:
                    filePerson.write(f"{larg},{nome},{idade},{peso}\n")

    def consultaPessoa(self, id=-1, nome="NoneValue", idade=-1, peso=-1.0):
        self.id = str(id)
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        matches = 0
        with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
            dados = []
            for count in filePerson.readlines():
                dados.append(count.strip("\n").split(","))
            for count in dados[1:]:
                filePerson.seek(0)
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

    def apagarPessoa(self, busca):
        self.busca = busca
        with open(ARQUIVO_PESSOAS, "r", encoding=ENC) as filePerson:
            linhas = filePerson.readlines()
        for i, linha in enumerate(linhas):
            if busca in linha:
                linhas.pop(i)
                break
        with open(ARQUIVO_PESSOAS, "w+", encoding=ENC) as filePerson:
            for linha in linhas:
                filePerson.write(linha)

    def editarPessoa(self, busca, nomeN="NoneValue", idadeN=-1, pesoN=-1):
        self.busca = busca
        self.novoNome = nomeN
        self.novaIdade = idadeN
        self.novoPeso = pesoN
        with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
            linhas = filePerson.readlines()
            for count in linhas:
                if self.busca in count and self.novoNome != "NoneValue":
                    linhas[1] = self.novoNome
                elif self.busca in count and self.novaIdade != -1:
                    linhas[2] = self.novaIdade
                elif self.busca in count and self.novoPeso != -1:
                    linhas[3] = self.novoPeso
        with open(ARQUIVO_PESSOAS, 'w+', encoding=ENC) as filePerson:
            for count in linhas:
                filePerson.write(count)

obj1 = Pessoas()
obj1.editarPessoa("19,Silvia,24,62.0", "Carla", 22, 90.0)

# obj1.consultaPessoa(nome="c")

# 0 - ID
# 1 - Nome
# 2 - Idade
# 3 = peso
