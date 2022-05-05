a = input("Frase: ")
z = []
b = ['b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
c = len(a)
for i in range (c):
    if a[i].lower() in b:
        z.append(a[i])   
r=z
print(z)