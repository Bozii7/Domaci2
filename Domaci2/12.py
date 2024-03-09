# 12. Napisati program koji obrađuje dvocifreni broj na sledeći način:
# a. Ako je prva cifra veća od druge štampati razliku prve i druge cifre
# b. Ako je prva cifra manja od druge štampati zbir te dvije cifre
# c. Ako su cifre iste štampati njihov proizvod

broj = int(input("Unesi dvocifreni broj: "))

cif2 = broj % 10
cif1 = broj // 10

if cif1 > cif2:
    print(cif1 - cif2)
elif cif1 < cif2:
    print(cif1 + cif2)
else:
    print(cif1 * cif2)