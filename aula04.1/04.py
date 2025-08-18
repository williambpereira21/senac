#demonstração do uso de condicional match/case....
print('digite o número referente ao estado da moeda:')
print('1. flor de cunho')
print('2. soberba')
print('3.muito bem conservada')
print('5. outros estados')
estado=int(input())

match estado:
    case 1:
        print('perfeita! vou pagar 1.000.000,00!')
        case 2:
        print('quase perfeita! vou pagar 250.000,00!')
        case 3:
        print('que ótimo! vou pagar 30.000,00!')
        case 4:
        print('desculpe não posso aceitar nesse estado')
        case 5:
        print('desculpe não posso aceitar nesse estado')
        case _:
        print('desculpe opção não reconhecida')