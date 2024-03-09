# 57. Narcissistic Number je broj čija suma cifara (tog broja) stepenova sa njegovim brojem
# cifara daje isti taj broj.
# Primjer 1: 153 (3 cifre)
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# Primjer 2: 1634 (4 cifre):
# 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# Vaš program treba da štampa “Da” ili “Ne” u zavisnosti od toga da li je broj Narcissistic ili
# nije. Input je uvijek validan broj.

broj = input("Unesi broj: ")
n = len(broj)
broj = int(broj)
brojtemp = broj
s = 0

while broj > 0:
    cif = broj % 10
    s += cif ** n
    broj = broj // 10

if s == brojtemp:
    print("Da")
else:
    print("Ne")