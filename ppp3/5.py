a = input("Frase: ")
b = ["a", "e","i","o","u"]
z =[]
for i in range(len(a)):
    if a[i].lower() in b:
        z.append(a[i])
print (len(z))