a = input("Frase: ")
z = []
b = ["a","e","i","o","u"]
c = len(a)
for i in range (c):
    z.append(a[i])
    if a[i] in b:
        a.upper()[i]
        z.append(a[i])
print (z)
