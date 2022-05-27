while 0==0:
    x=int(input("Num: "))
    print("6 *",x, "es",x*6)
    n=1
    for i in range(10):
        print("6 *",n, "es",n*6)
        n+=1
    l=str(input("Desitja sortir (S/N): "))
    if l.lower() in {"s"}:
        break