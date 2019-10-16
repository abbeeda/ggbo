a=input("请输入年份：")
b=a[-1:]
c=int(a[:-1])
while b == "年":
   break
else:
   print("输入错误")
if c%4==0:
   if c%100==0:
      print("该年不是闰年")
   else:
      print("该年是闰年")
else:
   print("该年不是闰年")
