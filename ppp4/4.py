n = input("Frase: ")
z = n.split()
for i in range (len(z)):
    m = z[0]
for h in range(len(z)):
    if(z[h]>m):
        m = z[h]
print(m)
