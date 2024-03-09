# 26. Napisati program koji provjerava da li je korsnik unio binarni, oktalni, dekadni ili
# heksadecimalni broj. Binarni broj ima prefiks 0b, oktalni 0o, heksadecimalni 0x, a
# dekadni nema prefiks.

broj = input("Unesi broj: ")

if broj[0] == '0' and broj[1] == 'b':
    print("Broj je binarni.")
elif broj[0] == '0' and broj[1] == 'o':
    print("Broj je oktalni.")
elif broj[0] == '0' and broj[1] == 'x':
    print("Broj je heksadecimalni.")
else:
    print("Broj je dekadni.")