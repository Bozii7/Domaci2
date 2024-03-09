# 7. Takmičari su radili testove iz matematike i programiranja. Za svaki predmet dobili su
# određeni broj poena (cio broj od 0 do 50). Takmičari se rangiraju po ukupnom broju
# poena iz oba predmeta. Ako dva takmičara imaju isti broj poena, pobjednik je onaj koji
# ima više poena iz programiranja. Potrebno je napisati program koji određuje pobjednika
# takmičenja.

ocjena_matematika1 = int(input("Unesi broj poena iz mate za prvog takmicara: "))
ocjena_programiranje1 = int(input("Unesi broj poena iz prog za prvog takmicara: "))

ocjena_matematika2 = int(input("Unesi broj poena iz mate za drugog takmicara: "))
ocjena_programiranje2 = int(input("Unesi broj poena iz prog za drugog takmicara: "))

ukupno1 = ocjena_matematika1 + ocjena_programiranje1
ukupno2 = ocjena_matematika2 + ocjena_programiranje2

if ukupno1 > ukupno2:
    print("Pobjednik je prvi takmicar.")
elif ukupno1 < ukupno2:
    print("Pobjednik je drugi takmicar.")
else:
    if ocjena_programiranje1 > ocjena_programiranje2:
        print("Pobjednik je drugi takmicar.")
    elif ocjena_programiranje1 < ocjena_programiranje2:
        print("Pobjednik je drugi takmicar.")
    else:
        print("Pobjednici su obojica. ")