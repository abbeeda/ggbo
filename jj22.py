import random
b=random.randint(0,100)
a=1
while a<7:
    c=int(input(""))
    if c>b:
        print("偏大")
    if c<b:
        print("偏小")
    if c==b:
        print("正确")
    a+=1
print(b)