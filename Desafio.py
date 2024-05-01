from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
class Conta:
    def __init__(self, saldo, numero, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n #### Você não possui saldo suficiente! ####")
        elif valor > 0:
            self._saldo -= valor
            print(f"\n ==== Saque de R${valor} Realizado com Sucesso! ====")
            return True
        else:
            print("\n #### Valor informado invalido! ####")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n ==== Depósito de R${valor} Realizado com Sucesso! ===")
        else:
            print("#### Valor informado invalido! ####")
            return False
        
        return True
class ContaCorrente(Conta):
    def __init__(self, numero, cliente,limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao['tipo'] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("#### Erro: Valor de saque maior que o limite permitido. ####")
        elif excedeu_saques:
            print("#### Erro: Número máximo de saques diarios excedido. ####")
        else:
            return super().sacar(valor)
    
    def __str__(self):
        return f'''
            Agencia: {self.agencia}
            C/C: {self.numero}
            Titular: {self.cliente.nome}
        '''
class Historico:
    def __init__(self) -> None:
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime("%d/%m/%Y %H:%M:%s")
            }
        )
class Transacao(ABC):
    @property
    def valor(self):
        pass
    @abstractmethod
    def registrar(self,conta):
        pass
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self.valor)
class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)