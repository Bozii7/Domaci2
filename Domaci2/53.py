# 53. Fudbal – Petar je posmatrao fudbalsku utakmicu i na papiru zapisivao rezultat sa
# semafora poslije svakog gola. Npr. mogući zapis je: 1:0, 1:1, 1:2, 2:2, 2:3. Zatim je Petar
# sabrao sve zapisane brojeve: 1+0+1+1+1+2+2+2+2+3=15. Na osnovu datog zbira,
# napišite program koji određuje koliko je golova bilo na utakmici. Ulaz: U jednom redu dat
# je cio broj N – Petrov zbir (1 ≤ N ≤1000). Izlaz: Štampati jedan cio broj – broj golova.

import random
broj_golova = int(input('Unesi broj golova: '))
lista = ['a', 'b']
a = 0
b = 0
suma = 0
while suma != broj_golova:
    if random.choice(lista) == 'a':
        a += 1
    else:
        b += 1
    suma += a + b
print(a)
print(b)
print(a+b)