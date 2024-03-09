# 36. Kreirati program koji unijeti string s (karakteri stringa alfabetski karakteri, mala slova)
# enkriptuje na sledeći način: ako je karakter suglasnik pretvara ga u 0, a ako je karakter
# samoglasnik pretvara ga u 1. Npr. za s = ‘abaae’ rezultat je 10111.

s = input("Unesi string: ")
s1 = ''
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'i' or s[i] == 'u':
        s1 = s1 + '1'
    else:
        s1 = s1 + '0'
print(s1)