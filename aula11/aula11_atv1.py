class pessoa:
    def __init__(self,nome,idade,altura):
     self.nome=nome
     self.idade=idade
     self.altura=altura

    def verificar(self):
       if self.idade >=18:
          print('você é maior de idade!')
       else:
          print('você é menor de idade!')

p=pessoa('william',21,1.78)

p.verificar()



#agora vou modificar para 5 pessoas

class pessoa1:
   def __init__(self,nome,idade,altura):
     self.nome=nome
     self.idade=idade
     self.altura=altura
   def verificar(self):
       if self.idade >=18:
          print('você é maior de idade!')
       else:
          print('você é menor de idade!')


pessoas=[]                           #aqui eu inicio a lista

for c in range(5):                      #pergunto 5 vezes o nome , idade e altura
         p1=input(f'digite o {c+1}nome:')
         i1=int(input(f'digite a {c+1}idade:'))
         a1=float(input(f'digite a {c+1} altura: '))

         pessoa=pessoa1(p1,i1,a1)                            #aqui crio o objeto que é pessoa
         pessoas.append(pessoa)

for p in pessoas:                                            #aqui digo que a variável p temporária vai ser o valor da lista pessoas

    
 p.verificar()                                              #aqui chamo a função verificar com o valor da lista pessoa
    





#atv 2




# cadastrar 5 funcionários-nome e salário
#2 são professores-disciplinas que lecionam
#nome dos funcionários que recebem acima de 2000
#nome dos professores que lecionam matemática
#escrever nome e salário de todos os funcionários





class funcionario:
   def __init__(self,nome,salario,admissao,materia):
      self.nome=nome
      self.salario=salario
      self.admissao=admissao
      self.materia=materia
   def salarios(self):
      if self.salario>=2000 :
         print(' recebe 2000') 
        


class professores(funcionario):                                                       #professor também fez assim
   def materia(self):
      if self.materia == 'matemática':
         print(f'{self.nome} ensina matemática')
         return


professor1=professores('joão','21/04/2001',2500,'matemática')
professor1.salario()
professor1.materia()