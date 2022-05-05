a = input("Frase: ")
z = []
b = ["a","e","i","o","u"]
c = len(a)
for i in range (c):
    if a[i].lower() in b:
        z.append(a[i].upper())
    else:
        z.append(a[i].lower())
print (z)
