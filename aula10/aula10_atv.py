#exe1
matriz = [[0, 0], [0, 0]]

soma = 0

print("Digite os valores para a matriz 2x2:")
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        soma += matriz[i][j]

media = soma / 4

print("\nMatriz 2x2:")
for linha in matriz:
    print(linha)

print(f"\nSoma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")

#exe2
numeros=[]
num1=int(input('digite números de 1 a 9 sem repetir:'))

while len(numeros)<9:
    n=int(input(f'digite o {len(numeros)+1}número:'))
    if n>=1 and n<=9 and n not in numeros:
        numeros.append(n)
    else:
        print('número inválido ou repetido.tente novamente.')

a=numeros[0]
b=numeros[1]
c=numeros[2]
d=numeros[3]
e=numeros[4]
f=numeros[5]
g=numeros[6]
h=numeros[7]
i=numeros[8]

print('matriz formada')
print(a,b,c)
print(d,e,f)
print(g,h,i)

linha1=a+b+c
linha2=d+e+f
linha3=g+h+i

coluna1=a+d+g
coluna2=b+e+h
coluna3=c+f+i

diagonal1=a+e+i
diagonal2=g+e+c


if (linha1 == 15 and linha2 == 15 and linha3 == 15 and
    coluna1 == 15 and coluna2 == 15 and coluna3 == 15 and
    diagonal1 == 15 and diagonal2 == 15):
      print("\nParabéns! Você criou um Quadrado Mágico!")
else:
    print("\nNão é um Quadrado Mágico. Tente novamente.")


#exe3

# Função para cadastrar jogadores (titulares ou suplentes)
def cadastrar_jogadores(qtd, tipo="titular"):
    jogadores = []
    print(f"\nCadastro dos {qtd} jogadores {tipo}:")
    for i in range(qtd):
        print(f"\nJogador {i+1}:")
        nome = input("Nome: ")
        numero = input("Número da camisa: ")
        posicao = input("Posição (opcional): ")
        if posicao.strip() == "":
            posicao = "Não informado"
        jogadores.append([nome, numero, posicao])
    return jogadores
