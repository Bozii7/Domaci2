# 41. Napisati program koji za unijetu listu L i vrijednost max vraća broj elemenata koji su
# manji od max iz te liste. Napomena: lista sadrži samo cijele brojeve
# Input: a = [1,2,3], max = 3; Output: 2
# Input: a = [-1, 0, 5], max = -2; Output: 0

niz = input("Unesi niz: ").split()
max = 0
br = 0
for i in range(len(niz)):
    niz[i] = int(niz[i])
    if niz[i] > max:
        max = niz[i]

for i in range(len(niz)):
    if niz[i] < max:
        br = br + 1
print(max)
print(br)


