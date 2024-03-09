#63. Za dati string koji sadrži praznine (blankove), odrediti najdužu riječ u stringu.

tekst = input("Unesite tekst: ").split()
najduza = ''

for i in tekst:
    if len(i) > len(najduza):
        najduza = i
print(najduza)
