# 37. Igrač nasumično bira listicu na kojoj se nalazi tekst sastavljen od karaktera 1, 0 i *.
# Karakter 1 nosi 1 poen, 0 nosi 0 poena, dok * nosi -1 poen. Napisati program koji
# provjerava da li je igrač u plusu.

tekst = input('Unesite tiket: ')
poeni = 0
for i in range(len(tekst)):
    if tekst[i] == '1':
        poeni += 1
    elif tekst[i] == '0':
        poeni += 0
    elif tekst[i] == '*':
        poeni -= 1
print(poeni)