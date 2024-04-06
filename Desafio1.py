menu = '''
### BANCO DIO ###

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao =="d":
        print("Deposito \n")
        deposito = float(input("Digite o valor de depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Deposito: R${deposito:.2f}")
            print(f"Deposito realizado com sucesso, saldo atual: R${saldo:.2f}")
        
        else:
            print("Valor de depósito inválido")
    
    elif opcao == "s":
        print("Saque \n")
        saque = float(input("Digite o valor de saque: "))
        
        if numero_saques < LIMITE_SAQUES:
            
            if saque <= saldo and saque <= 500:
                saldo -= saque
                numero_saques += 1
                extrato.append(f"Saque: R${saque:.2f}")
                print(f"Saque realizado com sucesso, saldo atual: R${saldo:.2f}")
            
            elif saque > saldo:
                print("Saldo Insuficiente")
            
            elif saque > 500:
                print("Limite permitido por saque: R$500,00")
        
        else:
            print("Número de saques diários excedido.")
    
    elif opcao == "e":
        print("===== Extrato =====\n")
        
        if len(extrato) != 0:
            
            for i in extrato:
                print(i)
        
        else:
            print("Nenhuma operação realizada ainda")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")