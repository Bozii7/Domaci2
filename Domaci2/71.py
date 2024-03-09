# 71. Kreirati program koji analizira zadatu listu brojeva i određuje koliko među njima postoji
# onih brojeva koji nakon primjene kvadratnog korijena zadržavaju svojstvo da budu cijeli
# brojevi. Program treba da prikaže ukupan broj takvih brojeva u listi.

from math import sqrt
from math import floor
brojevi = input('Unesite listu brojeva: ').split()
brojac = 0
for j in range(len(brojevi)):
    brojevi[j] = eval(brojevi[j])

for i in brojevi:
    if sqrt(i) == floor(sqrt(i)):
        brojac += 1
print(brojac)