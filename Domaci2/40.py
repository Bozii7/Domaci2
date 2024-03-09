# 40. Napisati program koji na osnovu niza cijelih brojeva računa apsolutnu sumu svih
# negativnih parnih elemenata za unijeti niz. Štampati sumu.
# Primjer:
# Input: [-2, 7, -5, 3, 1, -4]
# Output: 6 (|-2| + |-4|)

niz_brojeva = input('Unesite zeljeni niz: ').split()
for i in range(len(niz_brojeva)):
    niz_brojeva[i] = int(niz_brojeva[i])
suma = 0
for i in range(len(niz_brojeva)):
    if niz_brojeva[i] < 0 and niz_brojeva[i] % 2 == 0:
        suma += niz_brojeva[i]
print(abs(suma))
