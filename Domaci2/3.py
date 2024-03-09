# 3. Zamislimo da pravimo program koji treba da odluči da li student može da pristupi ispitu.
# Postoje dva uslova: student mora imati više od 75% prisustva na predavanjima i mora
# imati predate sve seminarske radove. Oba uslova moraju biti zadovoljena da bi student
# mogao pristupiti ispitu. Algoritam treba da štampa odgovarajuću poruku. Dodatak:
# prisustvo se unosi u procentima, a dio za seminarske radove na sledeci nacin -> 0
# predstavlja da bar jedan seminarski rad nike uradjen, a 1 da su svi seminarski radovi
# uradjeni.

prisustvo = float(input("Koliko % prisustva ima student: "))
seminarski_radovi = int(input("Unesi 1 ako si polozio sve seminarske, a 0 ako nijesi sve: "))

if prisustvo > 75.0 and seminarski_radovi == 1:
    print("Mozes pristupiti ispitu")
else:
    print("Ne mozes polagati ispit")