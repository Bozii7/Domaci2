# 6. Vaš zadatak je da napravite program kojim provjeravate da li se pčela kreće po žici. Žica
# se može predstaviti pravom y = 2 * x + 5, dok se pčela predstavlja tačkom (x, y).

x = float(input('Unesite prvu kordinatu pcelice: '))
y = float(input('Unesite druga kordinatu pcelice: '))

if y == 2 * x + 5:
    print('Nalazi se na zici!')
else:
    print('Ne nalazi se na zici!')