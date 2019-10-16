a=input("")
k=int(input("k:"))
list1=list(a)
c=1
while c<k:
   a=max(list1)
   list1.remove(a)
   c+=1
print(a)