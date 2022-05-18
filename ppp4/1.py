u = input("Frase: ")
r = []
for h in range(len(u)):
    l = len(u)-h
    r.append(u[l-1])
print (r)