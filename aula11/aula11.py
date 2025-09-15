class cliente:
    def __init__(self,titular,conta,saldo):
        self.titular=titular
        self.conta=conta
        self.saldo=saldo
    def apresentar(self):
        print('olá! eu sou :',self.titular)
        print('minha conta é',self.conta)
        print('e quero saber o meu saldo.')
        return
    
fulano=cliente('joão',423050205-21,25000.00)               #objeto recebe=classe('e os atributos')
fulano.apresentar()

print('de fato, você realmente é:',fulano.titular)
print('no momento, a sua conta possui R$',fulano.saldo)




#outro exemplo


class cliente:
    def __init__(self,titular,conta,saldo):

      self.titular=titular
      self.conta=conta
      self.saldo=saldo

class cliente_fisico(cliente):
    def apresentar(self):
        print('olá ! eu sou:',self.titular)
        print('minha conta é:',self.conta)
        print('e quero saber o meu saldo.')
        return
    
fulano=cliente_fisico('joão',423.050205-21,25000.00)
fulano.apresentar
print('de fato,você realmente é:',fulano.titular)
print('no momento, a sua conta possui R$',fulano.saldo)


#outro exemplo

from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __init__(self,titular,conta,saldo):

      self.titular=titular
      self.conta=conta
      self.saldo=saldo

class cliente_fisico(cliente):
    def apresentar(self):
        print('olá ! eu sou:',self.titular)
        print('minha conta é:',self.conta)
        print('e quero saber o meu saldo.')
        return
    
fulano=cliente_fisico('joão',423.050205-21,25000.00)
fulano.apresentar
print('de fato,você realmente é:',fulano.titular)
print('no momento, a sua conta possui R$',fulano.saldo)



#outro exemplo



from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __init__(self,titular,conta,saldo):

      self.titular=titular
      self._conta=conta
      self._saldo=saldo

class cliente_fisico(cliente):
    def apresentar(self):
        print('olá ! eu sou:',self.titular)
        print('minha conta é:',self._conta)
        print('e quero saber o meu saldo.')
        return
    
fulano=cliente_fisico('joão',423.050205-21,25000.00)
fulano.apresentar
print('de fato,você realmente é:',fulano.titular)
print('no momento, a sua conta possui R$',fulano._saldo)

#outro exemplo

class cliente:
    @abstractmethod
    def __init__(self,titular,conta,saldo):                            

      self.titular=titular
      self._conta=conta                                    #'_'encapsulamento antes da variável 
      self._saldo=saldo
    def apresentar(self):                              #esse não vai ser chamado por ser da classe pai 
        print('olá,eu sou a classe pai!')
        pass                                    #impede de retornar valor


class cliente_fisico(cliente):                          #classe derivada
    def apresentar(self):                               #esse vai ser chamado
        print('olá ! eu sou:',self.titular)
        print('minha conta é:',self._conta)
        print('e quero saber o meu saldo.')
        return
    
fulano=cliente_fisico('joão',423.050205-21,25000.00)
fulano.apresentar
print('de fato,você realmente é:',fulano.titular)
print('no momento, a sua conta possui R$',fulano._saldo)




