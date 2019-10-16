a=1
b=1
while b<10:
    p=a*b
    print(a,"*",b,"=",p)
    a+=1
    while a==10:
        a=1
        b+=1
        continue


