#47. Korisnik unosi tri broja. Naći minimum i maksimum među unijetim brojevima i rezultat
#prikazati korisniku.

max = 0
min = 0

a = int(input("Unesi broj: "))
b = int(input("Unesi broj: "))
c = int(input("Unesi broj: "))

if a > b and a > c:
    max = a
if b > a and b > c:
    max = b
else:
    max = c

if a < b and a < c:
    min = a
if b < a and b < c:
    min = b
else:
    min = c
print(min)
print(max)