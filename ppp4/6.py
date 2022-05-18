f = input("Frase: ")
z= f.split()
p = input("Paraula: ")
if p in z:
    for i in range (len(z)):
        if p == z[i]:
            print("si, es la ", i)
else:
    print("no")