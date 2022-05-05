a = input("Frase: ")
z = []
b = ["a","e","i","o","u"]
c = len(a)
for i in range (c):
    if a[i] in b:
        z.append(a[i])   
r=z
print(z)