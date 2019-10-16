a=input("身份证号：")
b=int(a[6:10])
c=a[10:12]
d=a[12:14]
e=int(a[17])
h=2019-b
f=e%2
if f==0:
    g="女"
else:
    g="男"
print ("出生于：",b,"年",c,"月",d,"日"\n "性别：",g\n"年龄：",h)