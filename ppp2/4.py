a =[1,2,3,4,5,6,7,8,9]
n=int(input("Num: "))
while n not in a:
    print ("No és un número del 1 al 9")
    n=int(input("Num: "))
else:
    print (n)