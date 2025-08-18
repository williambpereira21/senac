print('digite sua idade:')
idade= int(input())

if idade<18:
    print('você não é maior de idade!')
    print('não poderá realizar operações bancárias!')
    print('obrigado por escolher os nossos serviços!')

elif idade>=65:
    print('você está aposentado')
print('poderemos oferecer suporte técnico...')


else idade<18:
print(' você é maior de idade.')
print('portanto,pode realizar transações bancárias')
print('obrigado por escolher os nossos serviços!')