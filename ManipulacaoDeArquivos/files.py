ENC = "UTF-8"
ARQUIVO_PRODUTOS = r"ManipulacaoDeArquivos\Pessoas.txt"
try:
    with open(ARQUIVO_PRODUTOS, "x", encoding=ENC) as file:
        print(file.write("id,produto,preco\n"))
except FileExistsError:
    with open(ARQUIVO_PRODUTOS, 'r+', encoding=ENC) as file:
        if (file.read() == ""):
            file.write("id,produto,preco\n")
class Pessoas:
    def __init__(self):
        self.nome = 0
        self.idade = 0
        self.peso = 0
    def cadastraPessoa(self,nome:str,idade:int,peso:float):
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
                if "\n" not in file.readlines()[larg-1]:
                    file.write(f"\n{larg},{nome},{idade},{peso}\n")
                else:
                    file.write(f"{larg},{nome},{idade},{peso}\n")
    def consultaPessoa(self,id=0,nome="",idade=0,peso=0.0):
        self.id = str(id)
        self.nome = nome.capitalize()
        self.idade = int(idade)
        self.peso = float(peso)
        with open(ARQUIVO_PRODUTOS, "r+", encoding=ENC) as file:
            dados = []
            for n,count in enumerate(file.readlines(),0):
                dados.append(count.strip('\n').split(','))
            for count in dados[1:]:
                file.seek(0)
                if self.id == int(count[0]) or self.nome in count[1] or self.idade == int(count[2]) or self.peso == float(count[3]):
                    print(count)

# 0 - ID
# 1 - Nome
# 2 - Idade
# 3 = peso                
obj1 = Pessoas()
obj1.consultaPessoa(nome="Si")