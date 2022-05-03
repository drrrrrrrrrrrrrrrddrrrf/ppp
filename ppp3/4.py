a = input("Frase: ")
for i in range(len(a)):
    z = a[i]
    if 'aeiou' in str(z):
        print(z.upper())