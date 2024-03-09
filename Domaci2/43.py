# 43. Data je lista ocjena na predmetu likovno za sve učenike jednog odjeljenja osnovne
# škole. Ispostavilo se da nema učenika koji imaju ocjenu 1 i 2. Prebrojati koliko učenika
# ima ostale ocjene (za svaku ocjenu pojedinačno).

ocjene = input('Unesite zeljeni niz: ').split()
petice = 0
cetvorke = 0
trojke = 0
for i in range(len(ocjene)):
    ocjene[i] = eval(ocjene[i])
for i in range(len(ocjene)):
    if ocjene[i] == 5:
        petice += 1
    elif ocjene[i] == 4:
        cetvorke += 1
    elif ocjene[i] == 3:
        trojke += 1
    else:
        pass
print(f'Petica je: {petice}')
print(f'Cetvorki je: {cetvorke}')
print(f'Trojki je: {trojke}')