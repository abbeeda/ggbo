N=int(input(""))
a=1
p=0
while a<N:
   if a%3==0:
       p=p+a
   else:
        if a%5==0:
            p=p+a
   a+=1
print(p)
