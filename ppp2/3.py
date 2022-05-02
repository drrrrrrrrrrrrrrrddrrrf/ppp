a =[]
n=int(input("Num: "))
a.append(n)
z=sum(a)
while n!=0:
    n=int(input("Num: "))
    a.append(n)
    z=sum(a)
print (z)