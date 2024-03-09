# 22. Za unijetu tačku sa koordinata (x,y) provjeriti kom kvadratnu pripada u koordinatnom
# sistemu.

x = int(input('Unesite \'x\' kordinatu: '))
y = int(input('Unesite \'y\' kordinatu: '))

if x > 0 and y > 0:
    print('Pripada prvom kvadrantu.')
elif x < 0 and y > 0:
    print('Pripada drugom kvadrantu.')
elif x < 0 and y < 0:
    print('Pripada trecem kvadrantu.')
elif x > 0 and y < 0:
    print('Pripada cetvrtom kvadrantu.')
else:
    print('Vasa tacka je u kordinatnom pocetku.')