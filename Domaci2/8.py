# 8. Napisati program kojim se na osnovu datog prosjeka učenika prikazuje uspjeh učenika.
# Odličan uspjeh ima učenik čiji je prosjek veći ili jednak 4.5. Vrlodobar uspeh postiže
# učenik čiji je prosek veći ili jednak 3.5, a manji od 4.5, dobar uspeh se postiže za prosek
# koji je veći ili jednak 2.5 a manji od 3.5, dovoljan uspeh za prosek veći ili jednak 2, a
# manji od 2.5. Ako učenik ima neku jedinicu unijeće se prosjek 1, a uspeh mu je
# nedovoljan.

ocjene = input("Unesi ocjene ucenika: ").split()

for i in range(len(ocjene)):
    ocjene[i] = eval(ocjene[i])

if 1 not in ocjene:
    uspjeh = sum(ocjene) / len(ocjene)
    if uspjeh >= 4.5:
        print('Odlican')
    elif uspjeh >= 3.5:
        print('Vrlodobar')
    elif uspjeh >= 2.5:
        print('Dobar')
    elif uspjeh >= 2:
        print('Dovoljan')
else:
    print('Nedovoljan')

