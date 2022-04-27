n=int(input("Num: "))
while n not in ["a"]:
    print("6 *",n, "es",n*6)
    n+=1
    r=input("Desitja sortir (S/N)? ")
    if r in ["S","s"]:
        break