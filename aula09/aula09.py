lista = []
lista_inteiros=[1,2,3,4,5]
lista_caracteres=['maçã','banana','cereja']
lista_mista = [1,'olá',3.14,True]

tupla_semana=('segunda','terça','quarta')
tupla_fibonacci=(1,2,3,5,8,13,21)

print(lista_inteiros)
print(lista_caracteres[0])         #maçã
print(lista_mista[1])              #olá
print(tupla_semana[2])             #terça
print(tupla_fibonacci)




print('vou montar a marmita com 5 alimentos')
marmita=['feijão','arroz','legumes','salada','carne']
print('eis, a nossa recomendação:',marmita)

resposta=input('quer montar uma marmita diferente (s/n)?')
if resposta=='s':
    for x in range(len(marmita)):                                  #len contabiliza em marmita onde vai ser contado de 0,1,2,3,4

        print(f'digite o {x+1} o item do cardápio:')               #x+1 é pra contar apartir de 1,2,3,4,5 em vez de 0,1,2,3,4
        marmita[x]=input()
    print('a marmita montada foi:',marmita)
    print('o três primeiros itens foram ',marmita[0:3])
    print('o último item da marmita foi:',marmita[-1])

else:
    print('ok. você decide...')



#exemplos
print(marmita[:])
print(marmita[2:3])
print(marmita[0:4:2])
print(marmita[-3:-1])





print('eis, os meus maiores sonhos...')
sonhos=['1. me divertir na disney','2.me banhar na praia de sepetiba','3.tirar férias em paris','4.fazer compras no west shopping','5.ver as pirâmides do egito']
for x in sonhos:
    print(x)

print('ops , não quero sepetiba!')                                #quando tira sepetiba muda a ordem
del(sonhos[1])
print('e nem west shopping!')                                     #agora west shopping é 2
del(sonhos[3])

print('conferindo os sonhos...')
for x in sonhos:
    print(x)

numeros=[7,2,9,6,5,0,3,8,1,4]
palavras=['olá','alô','hei','uau','ops']

print('quantas variáveis possui:')
print('números:',len(numeros))
print('palavras:',len (palavras))

print('vamos reordenar estas listas?')
print(sorted(numeros))                                           #sorted reordena pondendo ser em ordem alfabética
print(sorted(palavras))

print('o somatório de número:',sum (numeros))
print('qual é o maior valor?',max (numeros))
print('qual é a primeira palavra?',min(palavras))



#outro exemplo

inss = ['maria','manoel','josé','isabela']
print('eis, a fila do inss:',inss)

novo=input('insira mais uma pessoa:')
inss.append(novo)
print('conferindo a nova lista',inss)

print('vou tirar a última pessoa desta lista...')
especial=inss.pop()

print('agora,vou colocá-la na frente de todos!')
inss.insert(0,especial)
print('conferindo a lista:',inss)

print('maria não gostou e reclamou...')
inss.remove('maria')
print('e agora, ela saiu "pê da vida"',inss)

print('para  não ter mais reclamação,vamos atender...')
inss.sort()
print('...em ordem alfabética',inss)
print('onde está esta nova pessoa chamada',especial,'?')
print('ela agora ficou na posição',inss.index(especial)+1,"!")

#outro exemplo

print('vou almoçar em um restaurante a quilo!')


original=['arroz','feijão','batata','alface','frango']
print('eis,a minha comida',original)
derivada=original[:]
print('meu amigo irá comer também:',derivada)
print('vou alterar as opções  sem ele ver...')
original.remove('arroz')
original.remove('feijão')
original.remove('alface')
original.append('picanha')
original.append('linguiça')

print('amiguinho,me mostre o que você vai comer?')
print('claro ! dá uma conferida',derivada)