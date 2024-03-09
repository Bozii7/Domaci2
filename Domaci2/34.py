#34. Napisati program koji iz teksta izvlači cifre i računa njihov proizvod.

tekst = input("Unesi tekst: ")
p = 1

for i in range(len(tekst)):
    if(tekst[i] >= '0' and tekst[i] <= '9'):
        p = p * int(tekst[i])
print(p)