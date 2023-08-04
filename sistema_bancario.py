from datetime import datetime

#como o saque aparece em duas situações diferentes, criei uma função.
def funcao_saque():
  global numero_de_saques
  global extrato
  global data_ultimo_saque
  global saldo

  print("""Bem vindo(a) a sua área de saque.
Segue modelo de como deve ser inserido o valor a ser retirado: 45.67
Use ponto final (.) para separar a casa decimal.
  """)
  while True:
    try:
      saque = float(input("Insira o valor que deseja sacar: "))
      if saque > 500:
        print("Limite máximo por saque é de R$ 500.00\n")
      elif saque > saldo:
        print(f"Você não possue saldo suficiente. Seu saldo atual é de {saldo:.2f}.\n")
      else:
        saque_formatado = f"R$ {saque:.2f}"
        extrato = extrato + "Saque:    " + data_formatada.ljust(25, '-') + saque_formatado + "\n"
        data_ultimo_saque = data_formatada
        saldo -= saque
        numero_de_saques += 1
        break      
    except ValueError:
      print("Valor inválido! Use apenas números para os valores e separe o real do centavo com ponto final (.)")

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
          print("Valor inválido! Use apenas números para os valores e separe o real do centavo com ponto final (.)")
  
  elif opcao == 2:
    if data_ultimo_saque != data_formatada:
      numero_de_saques = 0
      funcao_saque()

    else:
      if numero_de_saques == 3:
        print("Você alcançou seu limite de saque diário. Retornar amanhã.")
      else:
        funcao_saque()
 
  elif opcao == 3:
    print(extrato)
    print(f"Seu saldo atual é de R$ {saldo:.2f}")
  elif opcao == 0:
    break
  else:
    print("Opção inválida, tente novamente!")