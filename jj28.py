a=input("")
class Doge:
    def bark(self):
        return "喵喵喵"
    def creep(self):
        return "爬爬爬"
x=Doge()
if a=="Doge.bark()":
    print("Doge.bark--",x.bark())
else:
    if a=="Doge.creep()":
        print("Doge.creep()",x.creep())
    else:
        print("输入错误")