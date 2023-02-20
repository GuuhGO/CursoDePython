import abc
import datetime as DaTi
class Autenticavel:
    def autentica(self,senha):
        if self._senha == senha:
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado")
            return False
class Cliente(Autenticavel):
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
class Conta:
    _total_contas = 0
    __slots__ = ['_numero',	'_titular',	'_saldo', '_limite', '_historico']
    def __init__(self,numero,cliente,saldo,limite=500.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1
    def deposita(self,valor):
        self._saldo += valor
        self._historico.transacoes.append(f"{DaTi.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito de %.2f" % valor)
    def saca(self,valor):
        if (valor < 0):
            print("Valor de saque não pode ser negativo!")
            return False
        elif (valor > self._saldo):
            print("Saldo insuficiente")
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append(f"{DaTi.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque de R$%.2f" % valor)
            return True
    def extrato(self):
        print(f"Número da conta: {self._numero}\nNome: {self._titular.nome}\nSaldo: {self._saldo}", end="\n\n")
        self._historico.transacoes.append(f"{DaTi.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Tirou extrato - saldo de R$%.2f" % self._saldo)
    def transferePara(self,destino,valor):
        
        if(self.saca(valor)):
            destino.deposita(valor)
            self._historico.transacoes.append(f"{DaTi.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Transferência de R$%.2f para a conta {destino._titular.nome}" % valor)
            return True
        else:
            return False
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
class Historico:
    def __init__(self):
        self.dataAbertura = DaTi.datetime.today().strftime("%d/%m/%Y - %H:%M:%S")
        self.transacoes = []
    def imprime(self):
        print(f"Data de abertura: {self.dataAbertura}")
        # print(f"Transações: {self.transacoes}")
        for t in self.transacoes:
            print(t)
        print('\n')
class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 0.15
class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario, senha, qtdGerenciados=0):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtdGerenciados = qtdGerenciados
    # def autentica(self,senha):
    #     if self._senha == senha:
    #         print("Acesso permitido")
    #         return True
    #     else:
    #         print("Acesso negado")
    #         return False
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000
class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    # def autentica(self, senha):
    #     pass
    def get_bonificacao(self): # ATENÇÃO PARA A ATUAL OBRIGATORIEDADE DE DEFINIR O METODO 'get_bonificacao()' EM TODAS AS SUBCLASSES DE FUNCIONÁRIO DEVIDO AO USO DO MÓDULO 'abc' PARA TORNAR O MÉTODO ABSTRATO
        return super().get_bonificacao() + 500
class SistemaInterno:
    def login(self, funcionario):
        if(hasattr(funcionario, 'autentica')):
            funcionario.autentica(funcionario._senha)
            return True
        else:
            print(f"{self.__class__.__name__} não é autenticável!")
            False
class ControleBonificacoes:
    def __init__(self, totalBonificacoes = 0):
        self._totalBonificacoes = totalBonificacoes
    def registra(self, funcionario):
        if(hasattr(funcionario, 'get_bonificacao')):
            self._totalBonificacoes += funcionario.get_bonificacao()
        else:
              print("Instância de {} não implementa o método get_bonificacao()".format(self.__class__.__name__))
    @property
    def totalBonificacoes(self):
        return self._totalBonificacoes

# Instanciando objetos
if __name__ == "__main__": #Verifica se o código está sendo executado como principal e não como um módulo importado
    diretor = Diretor('João', '111111111-11', 3000.0, '1234')
    gerente = Gerente('José', '222222222-22', 5000.0, '1235')
    cliente = Cliente('Maria', '333333333-33', '1236')
    sistema = SistemaInterno()
    sistema.login(diretor)
    sistema.login(gerente)
    sistema.login(cliente)