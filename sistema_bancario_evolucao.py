from datetime import datetime

def funcao_gerar_extrato(saldo,/,*,extrato):
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

def funcao_saque(*, valor, extrato, data_formatada, saldo, numero_de_saques):
    extrato = extrato + "Saque:    " + data_formatada.ljust(25, '-') + f"R$ {valor:.2f}" + "\n"
    ultima_data_de_saque = data_formatada
    saldo -= valor
    numero_de_saques += 1
    saida_texto("Operação realizada com sucesso!")
    return numero_de_saques, extrato, ultima_data_de_saque, saldo   

def funcao_depositar(valor, extrato, saldo, data_formatada, /):
    extrato = extrato + "Depósito: " + data_formatada.ljust(25, '-') + f"R$ {valor:.2f}" + "\n"
    saldo += valor
    saida_texto("Operação realizada com sucesso!")
    return saldo, extrato
            
def saida_texto(texto):
    print(texto)

#funções para cadastro do usuário
def cadastro_nome():
    while True:
        try:
            nome = input("Insira seu nome completo: ")
            return nome.upper()
        except ValueError:
            saida_texto("Valor inválido!")
def cadastro_data_nascimento():
    while True:
        try:
            data_nascimento = input("\nInsira sua data de nascimento conforme modelo 02/09/1991, incluindo as barras: ")
            if len(data_nascimento) == 10 and data_nascimento.count("/") == 2:
                return data_nascimento
            else:
                saida_texto("Data de Nascimento inválida. Digite conforme modelo DIA/MÊS/ANO.")
        except ValueError:
            saida_texto("Valor inválido! Insira apenas números.")
def cadastro_endereco():
    logradouro = input("\nDigite seu logradouro: ")
    numero = input("Digite seu número: ")
    bairro = input("Digite seu bairro: ")
    cidade = input("Digite seu cidade: ")
    estado = input("Digite a silga do seu estado: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}."
    return endereco
def cadastro_cpf():
    while True:
        try:
            cpf = input("\nInsira seu cpf contendo apenas números: ")
            teste_inteiro = int(cpf)
            if len(cpf) == 11:
                return cpf
            else:
                saida_texto("Quantidade de caracter inválido. Digite novamente.")
        except ValueError:
            saida_texto("Valor inválido! Insira apenas números.")
def funcao_verifica_cpf(lista_usuarios,opcao):
    cpf = cadastro_cpf()
    status = True
    for usuario in lista_usuarios:
        if usuario["CPF"] == cpf:
            status = False
            break
    if opcao == 4:
        return cpf, status
    else:
        if status == False:
            return cpf, status, usuario["Nome"]
        else:
            return cpf, status, None
    
                 
menu = '''
Olá! Estamos acessando sua conta bancária, digite a opção que deseja, sendo:
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Cadastro Usuário
[5] - Cadastro Conta
[0] - Sair

'''
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3
ultima_data_de_saque = ""
lista_usuarios = []
lista_contas = []
numero_conta = 1

while True:
    data_atual = datetime.now().date()
    data_formatada = data_atual.strftime("%d/%m/%Y")
    try:
        opcao = int(input(menu))

        if opcao == 1:
            saida_texto("\nBem vindo(a) a sua área de depósito.\nSegue modelo de como deve ser inserido o valor a ser depositado: 45.67\nUse ponto final (.) para separar a casa decimal.")
            valor = funcao_verifica_valor()
            if valor != 0:
                saldo, extrato = funcao_depositar(valor, extrato, saldo, data_formatada)     
        elif opcao == 2:
            saida_texto("\nBem vindo(a) a sua área de saque.\nSegue modelo de como deve ser inserido o valor a ser retirado: 45.67\nUse ponto final (.) para separar a casa decimal.")
            valor = funcao_verifica_valor()
            if ultima_data_de_saque != data_formatada:
                numero_de_saques = 0
            status = funcao_verifica_saque(valor, saldo, numero_de_saques, limite_de_saques, limite)
            if status == True and valor != 0:
                numero_de_saques, extrato, ultima_data_de_saque, saldo = funcao_saque(valor=valor, extrato=extrato, data_formatada=data_formatada, saldo=saldo, numero_de_saques=numero_de_saques)
        elif opcao == 3:
            funcao_gerar_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            saida_texto("\nBem vindo(a)!\nA seguir iremos captar seus dados pessoais, esteja com documentação em mãos para facilitar seu cadastro.")
            cpf, status_cpf = funcao_verifica_cpf(lista_usuarios, opcao)
            if status_cpf == True:
                dados_usuario = {
                    "CPF": cpf,
                    "Nome": cadastro_nome(),
                    "Nascimento": cadastro_data_nascimento(),
                    "Endereço": cadastro_endereco()
                }
                lista_usuarios.append(dados_usuario)
                saida_texto(f"\nObrigado Senhor(a) {dados_usuario['Nome']}. Seu cadastro foi realizado com sucesso!")
            else:
                saida_texto("CPF já cadastrado.")
        elif opcao == 5:
            saida_texto("\nBem vindo(a)!\nA seguir iremos criar sua conta, esteja com CPF em mãos para facilitar seu cadastro.")
            cpf, status_cpf, nome = funcao_verifica_cpf(lista_usuarios, opcao)
            if status_cpf == False:
                dados_conta = {"Agência": "0001", "Conta": numero_conta, "CPF": cpf, "Nome": nome}
                numero_conta += 1
                lista_contas.append(dados_conta)
                saida_texto(f"\nObrigado Senhor(a) {nome}. Sua conta foi criada com sucesso!")
                print(dados_conta)
            else:
                saida_texto("CPF não cadastrado. Selecionar a opção 4 do nosso Menu inicial e realizar cadastro do usuário.")
        elif opcao == 0:
            break
        else:
            saida_texto("\nOpção inválida, tente novamente!")
    except ValueError:
        saida_texto("Valor inválido. Insira apenas números conforme Menu.")