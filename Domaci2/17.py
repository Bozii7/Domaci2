# 17. Napisati program koji provjerava da li se od pravouganika poznatih dimenzija stranica
# mogu napraviti bar dva kvadrata čija je duzina ista kao i dužina pravouganika.

sirina = float(input('Unesite sirina pravougaonika: '))
duzina = float(input('Unesite duzinu pravougaonika: '))

if sirina % duzina == 0:
    print('Moze')
else:
    print('Ne moze')