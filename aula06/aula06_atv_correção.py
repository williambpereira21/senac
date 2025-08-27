f1=1;f2=2;x=0
while x <=2000:
    x=f1+f2
    f1=f2
    f2=x
    break
    print(x,end="")