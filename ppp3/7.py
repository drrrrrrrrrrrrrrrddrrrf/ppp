n=int(input("Num: "))
r=[]
x=[]
for i in range(n):
    z=int(input("Num: "))
    if z%2 == 0:
        r.append(z)
    else:
        x.append(z)
print(r, " Son parells. ",x,"  No son parells. ")