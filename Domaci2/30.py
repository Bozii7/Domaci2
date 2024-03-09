# 30. Napisati program koji računa zbir parnih i proizvod neparnih brojeva od 1 do n. Broj n
# unosi korisnik.
# a. Štampati taj zbir i proizvod.
# b. Štampati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta.

n = int(input("Unesi broj: "))

brp = 0
brn = 0
s = 0
p = 1

for i in range(1, n):
    if i % 2 == 0:
        s = s + i
        brp = brp + 1
    else:
        p = p * i
        brn = brn + 1

print("Suma je ", s)
print("Proizvod je ", p)

print("Parnih ima ", brp)
print("Neparnih ima ", brn)

