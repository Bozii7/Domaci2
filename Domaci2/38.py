# 38. Napisati program koji za unijeti string s (provjeriti da li je karakter cifra) enkriptuje na
# sledeći način: ako je karakter paran broj pretvara se u 0, a ako je karakter neparan broj
# pretvara se u 1. Npr. za s = ‘15023’ rezultat je 11001.

s = input("Unesi string: ")
s1 = ''
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        s1 = s1 + '0'
    else:
        s1 = s1 + '1'
print(s1)
