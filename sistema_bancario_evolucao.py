from datetime import datetime

def funcao_verifica_valor():
    while True:
        try:
            valor = float(input("Insira o valor que deseja sacar: "))
            if valor < 0:
                print("O valor precisa ser maior que zero.\n")
            else:
                return valor
        except ValueError:
            print("Valor inválido! Use apenas números para os valores e separe o real do centavo com ponto final (.)")    

def funcao_saque(valor, extrato, data_formatada, saldo, numero_de_saques, limite_de_saques, limite):
    if valor > limite:
        print("Limite máximo por saque é de R$ 500.00\n")
    elif valor > saldo:
        print(f"Você não possue saldo suficiente. Seu saldo atual é de {saldo:.2f}.\n")
    elif numero_de_saques == limite_de_saques:
        print("Você alcançou seu limite de saque diário. Retornar amanhã.")
    else:
        saque_formatado = f"R$ {valor:.2f}"
        extrato = extrato + "Saque:    " + data_formatada.ljust(25, '-') + saque_formatado + "\n"
        data_ultimo_saque = data_formatada
        saldo -= valor
        numero_de_saques += 1
        return numero_de_saques, extrato, data_ultimo_saque, saldo   

def funcao_depositar(valor,extrato,saldo,data_formatada):
    deposito_formatado = f"R$ {valor:.2f}"
    extrato = extrato + "Depósito: " + data_formatada.ljust(25, '-') + deposito_formatado + "\n"
    saldo += valor
    return saldo,extrato
            
def menu_sacar():
    print("Bem vindo(a) a sua área de saque.")
    print("Segue modelo de como deve ser inserido o valor a ser retirado: 45.67")
    print("Use ponto final (.) para separar a casa decimal.")

def menu_depositar():
    print("Bem vindo(a) a sua área de depósito.")
    print("Segue modelo de como deve ser inserido o valor depositado: 45.67")
    print("Use ponto final (.) para separar a casa decimal.")

menu = '''
Olá! Estamos acessando sua conta bancária, digite a opção que deseja, sendo:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

'''
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3
data_ultimo_saque = ""

while True:
    data_atual = datetime.now().date()
    data_formatada = data_atual.strftime("%d/%m/%Y")
    opcao = int(input(menu))

    if opcao == 1:
        menu_depositar()
        valor = funcao_verifica_valor()
        saldo,extrato = funcao_depositar(valor,extrato,saldo,data_formatada)  
       
    elif opcao == 2:
        menu_sacar()
        valor = funcao_verifica_valor
        if data_ultimo_saque != data_formatada:
            numero_de_saques = 0
        numero_de_saques, extrato, data_ultimo_saque, saldo = funcao_saque(valor = valor, extrato = extrato, data_formatada = data_formatada, saldo = saldo, numero_de_saques = numero_de_saques, limite_de_saques = limite_de_saques, limite = limite)
    
    elif opcao == 3:
        print("Não foram eralizadas movimentações." if not extrato else extrato)
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == 0:
        break
    else:
        print("Opção inválida, tente novamente!")