# 49. Napisati program koji skraćuje string do unijete dužine. Na kraj stringa dodati ... Ako je
# unijeza dužina veća od same dužine stringa, na kraju stringa dodati samo ...
# Primjer 1:
# string: “abcde”, duzina: 2, štampa se “ab...”
# Primjer 2:
# string: “abcde”, duzina: 10, štampa se “abcde...”

tekst = input("Unesi string: ")
duzina = int(input("Unesi duzinu: "))
novi_tekst = ''

if len(tekst) <= duzina:
    novi_tekst = novi_tekst + '...'
else:
    for i in range(duzina):
        novi_tekst += tekst[i]
    novi_tekst = novi_tekst + '...'
print(novi_tekst)