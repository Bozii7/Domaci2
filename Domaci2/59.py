# 59. Napisati program koji za unijeti string s (karakteri stringa cifre od 0 do 9) enkriptuje na
# sledeći način: ako je karakter paran broj pretvara se u 0, a ako je karakter neparan broj
# pretvara se u 1. Npr. za s = ‘15023’ rezultat je 11001. Pomoć: Inicijalna vrijednost za
# dodatni string je “”, a onda se pomoću operatora + nadodaje 0 ili 1 u zavisnosti u
# ispunjenosti uslova.

s = input("Unesi string: ")
s1 = ''
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        s1 = s1 + '0'
    else:
        s1 = s1 + '1'
print(s1)
