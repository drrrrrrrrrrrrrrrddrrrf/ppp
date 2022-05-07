nota = float(input("Nota: "))
pernil = bool(input("Has comprat un pernil al professor? En cas que no, deixar en blanc: "))
if nota>=5:
    print("Aprobat")
elif pernil == True:
    print("Aprobat")
else:
    print("Suspes")