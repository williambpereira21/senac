#1 atv
print('Digite um valor para ver a tabuada dele:')
valor = int(input())

for i in range(1, 11):  # De 1 até 10 (inclusive)
    resultado = valor * i
    print(f'Valor de {valor} x {i} é: {resultado}')

 #2 atv
print('qual o melhor clube de futebol do brasil,digite sua resposta:')
melhor='flamengo' 
resposta=''
while resposta !=melhor:
   resposta =input('digite a respota:')
   print('resposta errada!')

print(f'{resposta}, correta!')

#3 atv
contagem_ano_novo=0
while contagem_ano_novo<10:
  contagem_ano_novo+=1
if contagem_ano_novo==10:
    print('feliz ano novo!')

#4 atv

a = 0
b = 1

print(a)

while b <= 2000:
    print(b)  
    proximo = a + b
    a=b
    b=proximo                                                      

   
   
