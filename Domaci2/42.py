# 42. Dat je niz koji sadrži cijene proizvoda u jednom marketu. Market je za ovu nedelju odluči
# da spusti cijene svim proizvodima. Kolika će zarada marketa od tih proizvoda biti manja
# u odnosu na originalnu cijenu.

cijene = input("Unesi cijene: ").split()
for i in range(len(cijene)):
    cijene[i] = int(cijene[i])
zarada = 0
for i in range(len(cijene)):
    zarada = zarada + cijene[i] * 0.2
    cijene[i] = cijene[i] * 0.8
print(zarada)