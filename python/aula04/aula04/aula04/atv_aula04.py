saldo_da_Conta = float(input('Digite o seu saldo: '))
valor_do_produto = 300

if saldo_da_Conta > valor_do_produto:
    print('Você possui saldo suficiente para a compra')
    print('Portanto, poderá realizar a transação')
    print('Obrigado por escolher os nossos serviços!')

elif saldo_da_Conta == valor_do_produto:
    print('Seu saldo é igual ao produto')
    print('Se realizar a compra ficará com o saldo zerado')
    print('Ainda deseja realizar a transação?')
    print('1 - Sim')
    print('2 - Não')

    opção = int(input('Digite a opção (1 ou 2): '))

    match opção:
        case 1:
            print('A transação foi realizada')
        case 2:
            print('A transação não foi realizada')
        case _:
            print('Opção inválida. A transação não foi realizada.')

else:
    print('Você não possui saldo suficiente')
    print('Portanto, não poderá continuar com a compra')
    print('Obrigado por escolher os nossos serviços!')

