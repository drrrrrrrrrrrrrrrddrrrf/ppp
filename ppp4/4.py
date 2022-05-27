n = input("Frase: ")
z = n.split()
m = len(z[0])
r=z[0]
for h in range(len(z)):
    if(len(z[h])>m):
        m = z[h]
        r=z[h]
print(r)
