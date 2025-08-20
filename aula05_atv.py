time=input('digite o nome do time:')
posição=input('digite a posição do time:')

if posição==1:
   classificação=('seu time é campeão')

elif posição >=1 and posição<=6:
    classificação=('seu time foi pra libertadores')

elif posição >=7 and posição<=12:
   classificação=('seu time foi pra sul americana')

elif posição >=13 and posição<=16:
   classificação=('seu time foi desclassificado')

else:
    classificação=('posição inválida')


print(f"time:{time}")
print(f"posição:{posição}")
print(f"classificação:{classificação}")
