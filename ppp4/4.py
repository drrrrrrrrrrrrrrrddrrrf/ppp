n = input("Frase: ")
z = n.split()
r = []
for i in range (len(z)):
    r.append(len(z[i]))
    m = r[0]
for h in range(len(z)):
    if(r[h]>m):
        m = r[h]
        print(z[0+h])
