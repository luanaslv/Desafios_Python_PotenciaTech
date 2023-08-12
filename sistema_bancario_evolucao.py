from datetime import datetime

def funcao_verifica_valor():
    while True:
        try:
            valor = float(input("\nInsira o valor que deseja: "))
            if valor < 0:
               saida_texto("\nO valor precisa ser maior que zero.")
            else:
                valor_formatado = f"R$ {valor:.2f}"
                return valor,valor_formatado
        except ValueError:
            saida_texto("\nValor inválido! Use apenas números para os valores e separe o real do centavo com ponto final (.)")    

def funcao_saque(valor, extrato, data_formatada, saldo, numero_de_saques, limite_de_saques, limite, valor_formatado):
    if valor > limite:
        saida_texto("Limite máximo por saque é de R$ 500.00\n")
    elif valor > saldo:
        saida_texto(f"Você não possue saldo suficiente. Seu saldo atual é de {saldo:.2f}.\n")
    elif numero_de_saques == limite_de_saques:
        saida_texto("Você alcançou seu limite de saque diário. Retornar amanhã.")
    else:
        extrato = extrato + "Saque:    " + data_formatada.ljust(25, '-') + valor_formatado + "\n"
        data_ultimo_saque = data_formatada
        saldo -= valor
        numero_de_saques += 1
        saida_texto("Operação realizada com sucesso!")
        return numero_de_saques, extrato, data_ultimo_saque, saldo   

def funcao_depositar(valor,extrato,saldo,data_formatada,valor_formatado):
    extrato = extrato + "Depósito: " + data_formatada.ljust(25, '-') + valor_formatado + "\n"
    saldo += valor
    saida_texto("Operação realizada com sucesso!")
    return saldo,extrato
            
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
valor_formatado = ""

while True:
    data_atual = datetime.now().date()
    data_formatada = data_atual.strftime("%d/%m/%Y")
    opcao = int(input(menu))

    if opcao == 1:
        saida_texto("\nBem vindo(a) a sua área de depósito.\nSegue modelo de como deve ser inserido o valor a ser depositado: 45.67\nUse ponto final (.) para separar a casa decimal.")
        valor,valor_formatado = (funcao_verifica_valor())
        saldo,extrato = funcao_depositar(valor,extrato,saldo,data_formatada,valor_formatado)  
       
    elif opcao == 2:
        saida_texto("\nBem vindo(a) a sua área de saque.\nSegue modelo de como deve ser inserido o valor a ser retirado: 45.67\nUse ponto final (.) para separar a casa decimal.")
        valor, valor_formatado = funcao_verifica_valor()
        if data_ultimo_saque != data_formatada:
            numero_de_saques = 0
        numero_de_saques, extrato, data_ultimo_saque, saldo = funcao_saque(valor = valor, extrato = extrato, data_formatada = data_formatada, saldo = saldo, numero_de_saques = numero_de_saques, limite_de_saques = limite_de_saques, limite = limite, valor_formatado = valor_formatado)
    
    elif opcao == 3:
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == 0:
        break
    else:
        saida_texto("\nOpção inválida, tente novamente!")