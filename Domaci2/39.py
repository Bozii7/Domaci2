# 39. Narcissistic Number je broj čija suma cifara (tog broja) stepenova sa njegovim brojem
# cifara daje isti taj broj.
# Primjer 1: 153 (3 cifre)
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

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