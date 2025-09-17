print('Digite o número referente à escolha do filme:')
filme=int(input())
match filme:
   case 1: 
    print('1. Como treinar o seu dragão')
   case 2:
    print('2. Tubarão')
   case 3:
    print('3. Demon Slayer')
   case 4: 
    print('4. O Flautista Mágico')
   case 5: 
    print('5. Gente Grande')
   case _:
        print('Desculpe, opção não reconhecida.')


nota = int(input())

match nota:
    case 1:
        print('péssimo')
    case 2:
        print('ruim')
    case 3:
        print('razoável')
    case 4:
        print('bom')
    case 5:
        print('ótimo')
    case _:
        print('Desculpe, opção não reconhecida.')

#testar depois
#if nome_filme: print(f"Você escolheu o filme: {nome_filme}")
   # nota = int(input("Agora dê uma nota de 1 a 5 para o filme: "))