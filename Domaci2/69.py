# 69. Napisati program koji umanjujete zarade koje su veće od prosječne za 10 %, a zarade
# manje od prosječne uvećava za 10 %. Prikazati koliko zarada će biti iznad prosjeka
# nakon uvećanja/umanjenja.

zarade = input('Unesite zarade: ').split()
for i in range(len(zarade)):
    zarade[i] = eval(zarade[i])
brojac = 0
prosjek = sum(zarade)/len(zarade)

for i in zarade:
    if i > prosjek:
        i = i * 0.9
    else:
        i = i * 1.1
    if i > prosjek:
        brojac += 1
print(brojac)