for a in range(100,999):
    b=str(a)
    c=b[0]
    d=b[1]
    e=b[2]
    c=int(c)
    d=int(d)
    e=int(e)
    f=(c+d+e)**2
    if f==a:
        print(f,end=",\0")
    else:
        continue

