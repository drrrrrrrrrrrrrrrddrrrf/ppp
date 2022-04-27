pll = float(input("Preu del llapis: "))
qll = float(input("Quantitat de llapis: "))
pr = float(input("Preu del rotulador: "))
qr = float(input("Quantitat de rotulador: "))
r1 = pll * qll
r2 = pr * qr
total = r1 + r2 
print("Llapis",pll,"x",qll,"=",r1)
print("Retulador",pr,"x",qr,"=",r2)
print("Total: ", total,"€")
