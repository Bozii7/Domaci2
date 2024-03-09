# 19. U jednoj privatnoj školi uvedeno je pravilo kojim se određuje iznos popusta koji ostvaruju
# učenici prilikom upisa u narednu školsku godinu. Učenici sa odličnim uspehom ostvaruju
# popust od 40% ukupnog iznosa školarine, sa vrlodobrim 20% a sa dobrim 10%. Takođe,
# učenici koji su osvojili nagradu na nekom od državnih takmičenja ostvaruju popust od
# 30% ukupnog iznosa školarine. Ukoliko neki učenik ispunjava dva kriterijuma za popust
# primenjuje se kriterijum po kome je popust veći. Na osnovu punog iznosa školarine,
# prosečne ocene učenika i informacije o nagradama sa takmičenja odrediti iznos koji
# učenik treba da plati pri upisu u narednu školsku godinu.
# Ulaz: U prvoj varijabli nalazi se pun iznos školarine (realan broj), u drugoj prosječna
# ocjena učenika (realan broj od 2.0 do 5.0) a u trećoj 0 ukoliko učenik nema nagradu ili 1
# ukoliko je ima.
# Izlaz: Iznos školarine koju učenik treba da plati (zaokružen na najbliži cio broj) navodi se
# u jednoj linije standardnog izlaza.

skolarina = eval(input('Unesite iznos skolarine: '))
prosjek = eval(input('Unesite prosjecnu ocjenu ucenika: '))
nagrade = int(input('Unesite \'1\' ukoliko ucenik ima nagradu, u suprotnom unesite \'0\': '))
popust = 0
if 4.5 <= prosjek <= 5.0:
    popust += 0.4
elif 3.5 <= prosjek <= 4.5:
    popust += 0.2
elif 2.5 <= prosjek <= 3.5:
    popust += 0.1

if nagrade == 1:
    popust += 0.3
skolarina = skolarina * (1-popust)

print(f'Popust na skolarinu prilikom upisa u narednu godinu je {skolarina}')