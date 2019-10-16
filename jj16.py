a=5
b=8
c=3
d=(b^2-4*a*c)**1/2
if d<0:
    print("无实根")
else:
    e=(d-b)/2*a
    f=(b-d)/2*a
    print(e,f)