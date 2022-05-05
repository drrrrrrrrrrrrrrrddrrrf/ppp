a =[]
r =[]
n=int(input("Num: "))
for i in range(n):
    z=int(input("Num2: "))
    a.append(z)
for b in range (n):
    if a[b] < 0:
        r.append(a)
l=len(r)
print(l)