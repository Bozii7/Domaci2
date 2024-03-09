#68. Napisati program koji uvećava zarade koje su veće od prosječne zarade (prosjek liste)
#za X eura.

zarade = input('Unesite zarade: ').split()
povecanje = eval(input('Unesite povecanje: '))
for i in range(len(zarade)):
    zarade[i] = eval(zarade[i])
prosjek = sum(zarade)/len(zarade)
print(zarade)
for i in range(len(zarade)):
    if zarade[i] > prosjek:
        zarade[i] += povecanje

print(zarade)