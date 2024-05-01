from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

### Entidades ###
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

###  Interface de Usuário ###
def menu():
    menu = '''
        #### BANCO DIO ####
        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato
        [4]\tNova Conta
        [5]\tListar Contas
        [6]\tNovo Usuário
        [0]\tSair
        '''
    return input(textwrap.dedent(menu))

### Funcionalidades ###
def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n #### Cliente não possui conta ainda! ####")

def depositar(clientes):
    cpf = input("Informe o CPF do Cliente:\n")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print('#### Cliente não encontrado! ###')
        return
    
    valor = float(input('Informe o valor do deposito'))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do Cliente:\n")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print('#### Cliente não encontrado! ###')
        return
    valor = float(input('Informe o valor do saque'))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do Cliente:\n")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print('#### Cliente não encontrado! ###')
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n===== Extrato =====\n")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas transações ainda."
    else:
        for transacao in transacoes:
            extrao += f"\n {transacao['tipo']}: R${transacao['valor']:.2f}"    

    print(extrato)
    print(f'\n Saldo: R${conta.saldo:.2f}')
    print("************************")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do Cliente:\n")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print('#### Cliente não encontrado! Não foi possivel criar conta###')
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('==== Conta criada com susseço! ====')

def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))

def criar_cliente(clientes):
    cpf = input("Informe o CPF do Cliente:\n")
    cliente = filtrar_clientes(cpf, clientes)
    if cliente:
        print("\n #### CPF já cadastrado como cliente ####")
        return
    
    nome = input("Informe o nome completo: \n")
    data_nascimento = input("Informe a data de nascimento (dd-mm--aaaa): \n")
    endereco = input("Informe o endereco (Logradouro, Nº - Bairro - Cidade/ES): \n")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco, cpf=cpf,)
    clientes.append(cliente)

    print('\n ==== Cliente criado com Sucesso! ====')

### Aplicação ###
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao =='1':
            depositar(clientes)

        elif opcao =='2':
            sacar(clientes)
        
        elif opcao =='3':
            exibir_extrato(clientes)
        
        elif opcao =='4':
            numero_conta = len(contas) +1
            criar_conta(numero_conta, clientes, contas)
        elif opcao =='5':
            listar_contas(numero_conta, clientes,contas)
            
        elif opcao =='6':
            criar_cliente(clientes)

        elif opcao =='0':
            print("==== Obrigado por usar o Banco DIO! ====")
            break
        else:
            print("#### Opção Invalida ####")
            return
      
main()