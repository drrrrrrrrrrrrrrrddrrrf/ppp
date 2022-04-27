"""
Bucles


for x in range(0,4):
	print(x)



for lletra in "M14Programació":
	print(lletra)



for n in [2,5,7,4,1]:
	print(n)



n=1
while n<5:
	print(n)
	n+=1


for a in range(0,100):
	for b in range(0,100):
		print(a,b)


c=0
while c<10:
	print(c)
	c+=1
	if c==3:
		break


c=0
while c<10:
	c+=1
	if c%2==0:
		continue	
	print(c)


for c in range(0,10):
	if c%2==0:
		continue
	print(c)


for c in "Mare de deu senyor":
	if c=='e':
		pass
		print("També l'escrivim")
	print("La lletra és",c)


#escriure sols els 0
ll=[10,25,0,87,0,9,5,0]
for c in ll:
	if c==0:
		print(c)

"""
#Menu infinit
while 0==0:
	#Menú
	print("opcio 1")
	print("opcio 2")
	print("opcio 3: Sortir")

	opcio=input()
	if opcio=="1":
		print("Has escollit l'opcio1")
	elif opcio=="2":
		print("Has escollit l'opcio2")
	elif opcio=="3":
		print("A10")
		break
	else:
		print("Opció incorrecte")

"""