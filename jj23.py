<<<<<<< HEAD
import random
import string
code_str=string.ascii_letters+string.digits
def dde_code(len):
    return"".join(random.sample(code_str,len))
g=dde_code(len=4)
print(g)
c=input("")
if c==g:
    print("输入正确")
else:
    print("输入错误")
=======
import random
import string
code_str=string.ascii_letters+string.digits
def dde_code(len):
    return"".join(random.sample(code_str,len))
g=dde_code(len=4)
print(g)
c=input("")
if c==g:
    print("输入正确")
else:
    print("输入错误")
>>>>>>> c4107b7d195ae20fa506d622edecf008161c987b
