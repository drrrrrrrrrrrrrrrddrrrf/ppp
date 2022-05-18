u = input("Frase: ")
r = []
b = []
for h in range(len(u)):
    l = len(u)-h
    r.append(u[l-1])
for h in range(len(u)):
    b.append(u[h])
if r == b:
    print(u,", Es un palíndrom.")
else:
     print(u,", No es un palíndrom.")