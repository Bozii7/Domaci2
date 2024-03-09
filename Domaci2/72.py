# 72. Lista se sastoji od ocjena studenata na predmetu Ekonomija i razvoj. Koliko studenata je
# dobilo veću ocjenu od prosječne ocjene (ocjena 5 ne utiče na prosjek).

ocjene = input('Unesite listu brojeva: ').split()
prosjek = 0
for j in range(len(ocjene)):
    ocjene[j] = eval(ocjene[j])

for i in range(len(ocjene)):
    if ocjene[i] != 5:
        prosjek += ocjene[i]
prosjek = prosjek/(len(ocjene)-ocjene.count(5))
print(round(prosjek, 3))