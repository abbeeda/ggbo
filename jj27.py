class BMI:
    tall=0
    weigh=0
    def __init__(self,t,w):
        self.tall=t
        self.weigh=w
    def result(self):
        n=(self.tall/self.weigh)**2
        print("你的BMI是:",n)
a=int(input("你的身高是："))
b=int(input("你的体重是："))
p=BMI(a,b)
p.result()

        

