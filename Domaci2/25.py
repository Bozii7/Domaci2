# 25. Napisati program kojim se uklanja prvi i poslednji karakter teksta i štampa novi tekst.

s = input("Unesi tekst: ")

novi_tekst = s[1::]
n = len(novi_tekst)
novi_tekst = novi_tekst[:n - 1]
print(novi_tekst)
