import re

ENC = "UTF-8"
ARQUIVO_PESSOAS = r"ManipulacaoDeArquivos\Pessoas.txt"

class Pessoas:
    def __init__(self):
        print("Inicializando objeto")
        try:
            with open(ARQUIVO_PESSOAS, "x", encoding=ENC) as filePerson:
                print(filePerson.write("id,produto,preco\n"))
        except FileExistsError:
            with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
                if filePerson.read() == "":
                    filePerson.write("id,produto,preco\n")
    def cadastraPessoa(self, nome: str, idade: int, peso: float):
        with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
            larg = len(filePerson.readlines())
            verif = False
            filePerson.seek(0)
            for count in filePerson.readlines():
                if f"{nome},{idade},{peso}" in count:
                    verif = True
                    print("Dados já cadastrados!")
                    break
            if verif == False:
                filePerson.seek(0)
                if "\n" not in filePerson.readlines()[larg - 1]:
                    filePerson.write(f"\n{larg},{nome},{idade},{peso}\n")
                else:
                    filePerson.write(f"{larg},{nome},{idade},{peso}\n")

    def consultaPessoa(self, id=-1, nome="NoneValue", idade=-1, peso=-1.0):
        id = str(id)
        idade = int(idade)
        peso = float(peso)
        matches = 0
        with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
            dados = []
            for count in filePerson.readlines():
                dados.append(count.strip("\n").split(","))
            for count in dados[1:]:
                filePerson.seek(0)
                if (
                    re.search(rf"{id}", str(count[0])) != None
                    or re.search(rf"{nome.casefold()}", str(count[1])) != None
                    or re.search(rf"{nome.capitalize()}", str(count[1])) != None
                    or re.search(rf"{nome}", str(count[1])) != None
                    or re.search(rf"{idade}", str(count[2])) != None
                    or re.search(rf"{peso}", str(count[3])) != None
                ):
                    print(count)
                    matches += 1
            print(f"\n{matches} correspondência(s) encontrada(s)!\n")

    def apagarPessoa(self, busca):
        busca = busca
        with open(ARQUIVO_PESSOAS, "r", encoding=ENC) as filePerson:
            linhas = filePerson.readlines()
        for i, linha in enumerate(linhas):
            if busca in linha:
                linhas.pop(i)
                break
        with open(ARQUIVO_PESSOAS, "w+", encoding=ENC) as filePerson:
            for linha in linhas:
                filePerson.write(linha)

    def editarPessoa(self, buscaID:int, nomeN="NoneValue", idadeN=-1, pesoN=-1):
        with open(ARQUIVO_PESSOAS, "r+", encoding=ENC) as filePerson:
            linhas = filePerson.readlines()
            corresp = 0
            for n,count in enumerate(linhas[1:],1):
                if buscaID == int(count.split(',')[0]) and (nomeN != "NoneValue" or idadeN != -1 or pesoN != -1):
                    corresp += 1
                    linhas[n] = f"{count.split(',')[0]},{nomeN},{idadeN},{pesoN}\n"
            if corresp < 1:
                print("Nenhuma correspondência!")
        with open(ARQUIVO_PESSOAS, 'w+', encoding=ENC) as filePerson:
            for count in linhas:
                filePerson.write(count)

obj1 = Pessoas()
# obj1.cadastraPessoa("Jorge", 48, 110)
# obj1.consultaPessoa(id=7)
obj1.editarPessoa(buscaID=15, nomeN="Gustavo", idadeN=27, pesoN=95.0)

# 0 - ID
# 1 - Nome
# 2 - Idade
# 3 = peso
