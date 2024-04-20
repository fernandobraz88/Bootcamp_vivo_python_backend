###FUNÇÕES####

#Usuário e conta
def criar_usuario(usuarios_db):
    nome = input("Digite o nome completo do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    
    for usuario in usuarios_db:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário com esse CPF.")
            return
    
    novo_usuario = {'nome': nome, 'cpf': cpf}
    usuarios_db.append(novo_usuario)
    
    print("Usuário criado com sucesso.")

def filtrar_usuario(usuarios_db, cpf):
    for usuario in usuarios_db:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def criar_conta(agencia, contas_db, usuarios_db):
    cpf = input("Digite o CPF do usuário para criar a conta: ")
    usuario = filtrar_usuario(usuarios_db, cpf)
    if usuario:
        numero_conta = len(contas_db) + 1  
        nova_conta = {'agencia': agencia,'numero_conta': numero_conta, 'cpf': cpf, 'saldo': 0.0}
        contas_db.append(nova_conta)
        print(f"Conta criada com sucesso. Número da conta: {numero_conta}")
    else:
        print("Não foi possível criar a conta. CPF não encontrado.")

def listar_contas(contas_db):
    if not contas_db:
        print("Nenhuma conta registrada.")
        return
    for conta in contas_db:
        print(f"Agencia: {conta['agencia']},Número da Conta: {conta['numero_conta']}, CPF: {conta['cpf']}, Saldo: R${conta['saldo']:.2f}")

#Operações
def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: R${valor:.2f}")
        print(f"Deposito realizado com sucesso, saldo atual: R${saldo:.2f}")
    else:
        print("Valor de depósito inválido")

    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
            
            if valor <= saldo and valor <= 500:
                saldo -= valor
                numero_saques += 1
                extrato.append(f"Saque: R${valor:.2f}")
                print(f"Saque realizado com sucesso, saldo atual: R${saldo:.2f}")
            
            elif valor > saldo:
                print("Saldo Insuficiente")
            
            elif valor > limite:
                print("Limite permitido por saque: R$500,00")
        
    else:
        print("Número de saques diários excedido.")

    return saldo, extrato
    
def exibir_extrato(saldo,/,*,extrato):
    if len(extrato) != 0:
            
        for i in extrato:
            print(i)
        
    else:
        print("Nenhuma operação realizada ainda")
    
    print(f'Saldo: {saldo}')

###INTERFACE DE USUARIO##
def menu():
    menu_text= '''
        ### BANCO DIO ###
        [1] Novo Usuario
        [2] Nova Conta
        [3] Listar Contas
    
        [4] Depositar
        [5] Sacar
        [6] Extrato
        
        [0] Sair

        '''
    while True:
        alternativa = input(menu_text)
        if alternativa.isdigit() and 0 <= int(alternativa) <= 6:
            return int(alternativa)
        else:
            print("Por favor, digite uma opção válida.")

###IMPLEMENTAÇÃO###

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios_db = []
    contas_db = []

    while True:
        opcao = menu()
        
        if opcao == 1:
            print("\n===== Cadastrar Novo Usuário =====\n")
            criar_usuario(usuarios_db)

        elif opcao == 2:
            print("\n===== Criar Nova Conta =====\n")
            criar_conta(contas_db,usuarios_db)
        
        elif opcao == 3:
            print("\n===== Listar Contas =====\n")
            listar_contas(contas_db)
        
        elif opcao == 4:
            print("\n===== Deposito =====\n")
            valor = float(input("Digite o valor de depósito: "))
            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == 5:
            print("\n===== Saque =====\n")
            valor = float(input("Digite o valor de saque: "))

            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
        
        elif opcao == 6:
            print("\n===== Extrato =====\n")
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == 0:
            print("Obrigado por usar o Banco DIO!")
            break

main()