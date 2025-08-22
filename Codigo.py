primeiro_saque = segundo_saque = terceiro_saque = "Não realizado"
primeiro_deposito = segundo_deposito = terceiro_deposito = "Não realizado"
maximo_saque = 0
maximo_deposito = 0
total= 0.0

while True:
    print("Menu Bancário")
    print("1- Saque")
    print("2- Deposito")
    print("3- Extrato")
    print("4- Sair")
    resposta_usuario = input("Digite uma opção do menu acima: ")
    if resposta_usuario == "1":
        if maximo_saque < 3:
            print("Saques de no máximo R$500.00 e três vezes ao dia.")
            saque = float(input("Digite o valor do saque:"))
            if saque <= 500 and saque > 0 and saque <= total:
                total = total - saque
                maximo_saque += 1
                print(f"Saque de valor R${saque:.2f} realizado com sucesso.")
                if maximo_saque == 1:
                    primeiro_saque = f"{saque:.2f}"
                elif maximo_saque == 2:
                    segundo_saque = f"{saque:.2f}"
                elif maximo_saque == 3:
                    terceiro_saque = f"{saque:.2f}"
            else:
                print("Valor solicitado acima de R$500 ou saldo insuficiente.")
        else:
            print("Número máximo de saques realizados.")

    elif resposta_usuario == "2":
        if maximo_deposito <= 3:
            deposito = float(input("Digite o valor do deposito: "))
            if deposito > 0:
                total = deposito + total
                maximo_deposito += 1
                print(f"Deposito de valor R${deposito:.2f} realizado com sucesso.")
                if maximo_deposito == 1:
                    primeiro_deposito = f"R${deposito:.2f}"
                elif maximo_deposito == 2:
                    segundo_deposito = f"R${deposito:.2f}"
                elif maximo_deposito == 3:
                    terceiro_deposito = f"R${deposito:.2f}"
            else:
                print("Deposito não realizado.")
        else:
            print("Número máximo de depositos realizados.")

    elif resposta_usuario == "3":
        print("  _ Extrato Bancário: _")
        print(f"| Total disponível em conta: {total:.2f}")
        print("|___________")
        print("|  Saques:")
        print(f"| 1° Saque: {primeiro_saque}")
        print(f"| 2° Saque: {segundo_saque}")
        print(f"| 3° Saque: {terceiro_saque}")
        print("|____________")
        print("|  Depositos:")
        print(f"| 1° Depósito:{primeiro_deposito}")
        print(f"| 2° Depósito:{segundo_deposito}")
        print(f"| 3° Depósito:{terceiro_deposito}")
        print("|___________")

    elif resposta_usuario == "4":
        break

    else:
        print("Opção escolhida é inválida.")
