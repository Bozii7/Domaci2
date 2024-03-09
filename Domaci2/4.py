# 4. Kućni red zabranjuje pravljenje buke prije 6 časova, između 13 i 17 časova i nakon 22
# časa. Napiši program koji radnicima govori da li u nekom datom trenutku mogu da
# izvode bučnije radove

vrijeme = float(input("Unesi koliko je sati: "))

if vrijeme < 6 or 13 <= vrijeme < 17 or vrijeme > 22:
    print('Ne mozete raditi')
else:
    print("Mozete raditi.")
