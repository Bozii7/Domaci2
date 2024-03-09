# 44. Data je lista koja sadrži broj posjeta za poslednjih deset fudbalskih utakmica. Napisati
# program koji štampa koliko je bilo najviše posjeta u jednom danu.

utakmice = input('Unesite zeljeni niz: ').split()
for i in range(len(utakmice)):
    utakmice[i] = eval(utakmice[i])
print(max(utakmice))