# 51. Lozinka je jaka ako je njena dužina najmanje 8 simbola, i sadrži mala slova, velika slova
# i cifre. Napisati program koji provjerava da li je lozinka jaka. Ulaz: Unosi se jedna riječ,
# dužine ne veće od 100, koja sadrži mala i velika slova i cifre. Izlaz: Štampati YES ili NO.

loz = input("Unesi lozinku: ")
ind_mala = 0
ind_velika = 0
ind_cifre = 0

for i in range(len(loz)):
    if loz[i] >= 'a' and loz[i] <= 'z':
        ind_mala = ind_mala + 1
    if loz[i] >= 'A' and loz[i] <= 'Z':
        ind_velika = ind_velika + 1
    if loz[i] >= '0' and loz[i] <= '9':
        ind_cifre = ind_cifre + 1
if ind_mala > 0 and ind_velika > 0 and ind_cifre > 0:
    print("Jaka")
else:
    print("Nejaka")