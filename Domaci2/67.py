# 67. Napisati program koji provjerava koliko se određeni broj ponavlja u listi (taj broj unosi
# korisnik).

lista = input("Unesi brojeve: ").split()
broj = int(input("Unesi broj: "))
br = 0

for i in range(len(lista)):
    lista[i] = int(lista[i])
    if broj == lista[i]:
        br += 1

print(br)