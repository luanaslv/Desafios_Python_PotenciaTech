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
        print("""Bem vindo(a) a sua área de depósito.
    Segue modelo de como deve ser inserido o valor depositado: 45.67
    Use ponto final (.) para separar a casa decimal.
        """)
        while True:
        try:
            deposito = float(input("Insira o valor que deseja depositar: "))
            if deposito > 0:
            deposito_formatado = f"R$ {deposito:.2f}"
            extrato = extrato + "Depósito: " + data_formatada.ljust(25, '-') + deposito_formatado + "\n"
            saldo += deposito
            break
            else:
            print("O valor para depósito precisa ser maior que zero.\n")
        except ValueError:
            print("Valor inválido! Use apenas números para os valores e separe o real do centavo com ponto final (.)\n")
    
    elif opcao == 2:
        if data_ultimo_saque != data_formatada:
        numero_de_saques = 0
        numero_de_saques, extrato, data_ultimo_saque, saldo = funcao_saque(numero_de_saques, extrato, data_ultimo_saque, saldo)

        else:
        numero_de_saques, extrato, data_ultimo_saque, saldo = funcao_saque(numero_de_saques, extrato, data_ultimo_saque, saldo)
    
    elif opcao == 3:
        print("Não foram eralizadas movimentações." if not extrato else extrato)
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == 0:
        break
    else:
        print("Opção inválida, tente novamente!")