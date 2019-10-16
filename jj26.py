n1=0
n2=1
count=2
nterms=35
while count < nterms:
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print("第35项斐波拉契数列是：",nth)