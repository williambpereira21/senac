saldo = 0.0
meta = float(input("digite o valor da meta de saldo a ser alcançada: "))

total_depositos = 0
total_saques = 0
soma_movimentacoes = 0.0

tentativa = 1

for i in range(1, 1000):                 # limite de até 1000 transações
    if saldo >= meta:
        break                            # para o programa se a meta foi atingida

    print(f"\ntentativa {tentativa}")
    tentativa += 1

    print(f"saldo atual: r${saldo:.2f}")
    operacao = input("digite 'd' para depósito, 's' para saque ou 'q' para ignorar: ")

    if operacao in ['d', 'D']:
        valor = float(input("valor do depósito: "))
        if valor <= 0:
            print("valor inválido. o depósito deve ser maior que zero.")
            continue
        saldo += valor
        total_depositos += 1
        soma_movimentacoes += valor
        print(f"depósito de r${valor:.2f} realizado com sucesso.")

    elif operacao in ['s', 'S']:
        valor = float(input("valor do saque: "))
        if valor <= 0:
            print("valor inválido. o saque deve ser maior que zero.")
            continue
        if valor > saldo:
            print("saldo insuficiente para realizar o saque.")
        else:
            saldo -= valor
            total_saques += 1
            soma_movimentacoes += valor
            print(f"saque de r${valor:.2f} realizado com sucesso.")

    elif operacao in ['q', 'Q']:
        print("operação ignorada. continuando...")

    else:
        print("operação inválida. tente novamente.")

                                                                                          # relatório final
total_movimentos = total_depositos + total_saques
media = soma_movimentacoes / total_movimentos if total_movimentos > 0 else 0

print("\n=== relatório final ===")
print(f"saldo final: r${saldo:.2f}")
print(f"total de depósitos: {total_depositos}")
print(f"total de saques: {total_saques}")
print(f"média dos valores movimentados: r${media:.2f}")

