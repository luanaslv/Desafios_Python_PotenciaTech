from datetime import datetime

def extrato(saldo,extrato):
    saida_texto("Não foram realizadas movimentações." if not extrato else extrato)
    saida_texto(f"Seu saldo atual é de R$ {saldo:.2f}")

def funcao_verifica_valor():
    while True:
        try:
            valor = float(input("\nInsira o valor que deseja: "))
            if valor < 0:
               saida_texto("O valor precisa ser maior que zero. Digite zero para retornar ao MENU.")
            else:
                return valor
        except ValueError:
            saida_texto("Valor inválido! Use apenas números para os valores e separe o real do centavo com ponto final (.)")    

def funcao_verifica_saque(valor, saldo, numero_de_saques, limite_de_saques, limite):
    if valor > limite:
        saida_texto("Limite máximo por saque é de R$ 500.00")
    elif valor > saldo:
        saida_texto(f"Você não possue saldo suficiente. Seu saldo atual é de {saldo:.2f}.")
    elif numero_de_saques == limite_de_saques:
        saida_texto("Você alcançou seu limite de saque diário. Retornar amanhã.")
    else:
        return True

def funcao_saque(valor, extrato, data_formatada, saldo, numero_de_saques):
    extrato = extrato + "Saque:    " + data_formatada.ljust(25, '-') + f"R$ {valor:.2f}" + "\n"
    data_ultimo_saque = data_formatada
    saldo -= valor
    numero_de_saques += 1
    saida_texto("Operação realizada com sucesso!")
    return numero_de_saques, extrato, data_ultimo_saque, saldo   

def funcao_depositar(valor, extrato, saldo, data_formatada):
    extrato = extrato + "Depósito: " + data_formatada.ljust(25, '-') + f"R$ {valor:.2f}" + "\n"
    saldo += valor
    saida_texto("Operação realizada com sucesso!")
    return saldo, extrato
            
def saida_texto(texto):
    print(texto)

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
        saida_texto("\nBem vindo(a) a sua área de depósito.\nSegue modelo de como deve ser inserido o valor a ser depositado: 45.67\nUse ponto final (.) para separar a casa decimal.")
        valor = funcao_verifica_valor()
        if valor != 0:
            saldo, extrato = funcao_depositar(valor, extrato, saldo, data_formatada)  
       
    elif opcao == 2:
        saida_texto("\nBem vindo(a) a sua área de saque.\nSegue modelo de como deve ser inserido o valor a ser retirado: 45.67\nUse ponto final (.) para separar a casa decimal.")
        valor = funcao_verifica_valor()
        if data_ultimo_saque != data_formatada:
            numero_de_saques = 0
        status = funcao_verifica_saque(valor, saldo, numero_de_saques, limite_de_saques, limite)
        if status == True and valor != 0:
            numero_de_saques, extrato, data_ultimo_saque, saldo = funcao_saque(valor=valor, extrato=extrato, data_formatada=data_formatada, saldo=saldo, numero_de_saques=numero_de_saques)
    
    elif opcao == 3:
        extrato(saldo, extrato=extrato)
    elif opcao == 0:
        break
    else:
        saida_texto("\nOpção inválida, tente novamente!")
